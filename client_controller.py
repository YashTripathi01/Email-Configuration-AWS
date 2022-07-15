from datetime import datetime


def client_email(first_name, last_name, msg):
    return f'''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Emailer</title>
    </head>
    <body>
        <table
            style="
                width: 700px;
                margin: 0 auto;
                min-width: 700px;
                max-width: 700px;
                background-color: #f2f2f2;
                padding: 50px 50px 28px 50px;
            "
        >
            <tr>
                <td>
                    <table
                        style="
                            width: 600px;
                            margin: 0 auto;
                            min-width: 600px;
                            max-width: 600px;
                            background-color: #f2f2f2;
                        "
                    >
                        <tbody>
                            <tr>
                                <td bgcolor="#fff">
                                    <table
                                        style="
                                            padding: 20px 30px 30px 30px;
                                            background-color: #fff;
                                            border: none;
                                            font-family: Arial;
                                        "
                                    >
                                        <tr>
                                            <td
                                                style="
                                                    padding: 0 0 19px 0;
                                                    border: none;
                                                "
                                            >
                                                <table width="100%">
                                                    <tr>
                                                        <td>
                                                            <img
                                                                src="http://ui.openspace.website/akshay/fg-client/img/Header.png"
                                                                alt="Feright Gain"
                                                                height="50px"
                                                                width="153.7px"
                                                            />
                                                        </td>
                                                        <td
                                                            align="right"
                                                            width="50%"
                                                            style="
                                                                font-size: 11px;
                                                            "
                                                        >
                                                            <span
                                                                >Date:
                                                                <span
                                                                    style="
                                                                        font-size: 11px;
                                                                        font-weight: 600;
                                                                        font-family: Arial;
                                                                    "
                                                                    >{datetime.now().date()}</span
                                                                ></span
                                                            >
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td
                                                style="
                                                    background-color: #335291;
                                                    height: 0.5px;
                                                    padding: 0;
                                                    width: 540px;
                                                "
                                            ></td>
                                        </tr>
                                        <tr>
                                            <td
                                                align="center"
                                                style="
                                                    padding-top: 29.8px;
                                                    padding-bottom: 13.3px;
                                                "
                                            >
                                                <span
                                                    style="
                                                        font-size: 18px;
                                                        font-weight: normal;
                                                        font-weight: 600;
                                                        font-family: Arial;
                                                    "
                                                    >Dear,
                                                    <span style="color: #335291"
                                                        >{first_name} {last_name}</span
                                                    ></span
                                                >
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="center">
                                                <img
                                                    src="http://ui.openspace.website/akshay/fg-client/img/checked.png"
                                                    alt="checked"
                                                    style="
                                                        width: 107.1px;
                                                        height: 72px;
                                                    "
                                                />
                                            </td>
                                        </tr>
                                        <tr>
                                            <td
                                                align="center"
                                                style="padding-top: 19.7px"
                                            >
                                                <span
                                                    style="
                                                        font-size: 22px;
                                                        font-weight: 600;
                                                        font-family: Arial;
                                                    "
                                                    >Thank you!</span
                                                >
                                            </td>
                                        </tr>
                                        <tr>
                                            <td
                                                align="center"
                                                style="
                                                    border: none;
                                                    padding-top: 13px;
                                                    padding-bottom: 21.5px;
                                                    font-size: 14px;
                                                    font-family: Arial;
                                                "
                                            >
                                                <span
                                                    >We have received your
                                                    message. Our representative
                                                    <br />
                                                    will get in touch with you
                                                    soon.</span
                                                >
                                            </td>
                                        </tr>
                                        <tr>
                                            <td
                                                style="
                                                    background-color: #a8c8e6;
                                                    height: 1px;
                                                    padding: 0;
                                                    width: 540px;
                                                "
                                            ></td>
                                        </tr>
                                        <tr>
                                            <td
                                                style="
                                                    padding-top: 21.5px;
                                                    padding-bottom: 7px;
                                                "
                                            >
                                                <span
                                                    style="
                                                        font-size: 16px;
                                                        font-weight: normal;
                                                        line-height: 1.31;
                                                        color: #179ad2;
                                                        font-family: Arial;
                                                    "
                                                    >Message Details</span
                                                >
                                            </td>
                                        </tr>
                                        <tr>
                                            <td
                                                style="
                                                    padding: 30px;
                                                    border-radius: 10px;
                                                    background-color: rgba(
                                                        79,
                                                        166,
                                                        210,
                                                        0.1
                                                    );
                                                "
                                            >
                                                <span
                                                    style="
                                                        font-size: 12px;
                                                        line-height: 1.75;
                                                        font-family: Arial;
                                                    "
                                                >
                                                    {msg}
                                                </span>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <table
                                        style="
                                            margin-top: 8px;
                                            padding: 30px 30px 27px 30px;
                                            background-color: #fff;
                                            border: none;
                                            font-family: Arial;
                                            width: 100%;
                                        "
                                    >
                                        <tr>
                                            <td align="center">
                                                <span
                                                    style="
                                                        font-size: 18px;
                                                        font-weight: 600;
                                                        font-family: Arial;
                                                    "
                                                    >Questions? Reach us</span
                                                >
                                            </td>
                                        </tr>
                                        <tr>
                                            <td
                                                style="
                                                    padding-top: 21px;
                                                    padding-bottom: 21.8px;
                                                "
                                            >
                                                <table width="100%">
                                                    <tr>
                                                        <td
                                                            align="center"
                                                            valign="top"
                                                            style="width: 33%"
                                                        >
                                                            <img
                                                                src="http://ui.openspace.website/akshay/fg-client/img/location.png"
                                                                alt="pin"
                                                                width="7.9px"
                                                                height="11.3px"
                                                                style="
                                                                    margin-right: 6.1px;
                                                                "
                                                            /><span
                                                                style="
                                                                    font-size: 12px;
                                                                    line-height: 1.5;
                                                                    color: #787e84;
                                                                "
                                                                >Address</span
                                                            >
                                                            <p
                                                                style="
                                                                    margin: 0;
                                                                    padding-top: 6px;
                                                                    font-size: 11px;
                                                                    font-weight: 500;
                                                                    line-height: 1.36;
                                                                "
                                                            >
                                                                B-604 Damji
                                                                Shamji Corporate
                                                                Square Off A G
                                                                Link Road , Next
                                                                to Kanara
                                                                Business Centre
                                                                Pant Nagar
                                                                Ghatkopar East
                                                                Mumbai City
                                                                Maharashtra-
                                                                400075
                                                            </p>
                                                        </td>
                                                        <td
                                                            align="center"
                                                            valign="top"
                                                            style="width: 33%"
                                                        >
                                                            <img
                                                                src="http://ui.openspace.website/akshay/fg-client/img/call.png"
                                                                alt="pin"
                                                                width="11px"
                                                                height="11px"
                                                                style="
                                                                    margin-right: 5px;
                                                                "
                                                            /><span
                                                                style="
                                                                    font-size: 12px;
                                                                    line-height: 1.5;
                                                                    color: #787e84;
                                                                "
                                                                >Phone</span
                                                            >
                                                            <p
                                                                style="
                                                                    margin: 0;
                                                                    padding-top: 6px;
                                                                    font-size: 11px;
                                                                    font-weight: 500;
                                                                    line-height: 1.36;
                                                                "
                                                            >
                                                                <a
                                                                    href="tel:3075550133"
                                                                    style="
                                                                        text-decoration: none;
                                                                        color: #000;
                                                                    "
                                                                    >(307)
                                                                    555-0133</a
                                                                >
                                                            </p>
                                                        </td>
                                                        <td
                                                            align="center"
                                                            valign="top"
                                                            style="width: 33%"
                                                        >
                                                            <img
                                                                src="http://ui.openspace.website/akshay/fg-client/img/mail.png"
                                                                alt="pin"
                                                                width="14px"
                                                                height="11px"
                                                                style="
                                                                    margin-right: 6px;
                                                                "
                                                            /><span
                                                                style="
                                                                    font-size: 12px;
                                                                    line-height: 1.5;
                                                                    color: #787e84;
                                                                "
                                                                >Email</span
                                                            >
                                                            <p
                                                                style="
                                                                    margin: 0;
                                                                    padding-top: 6px;
                                                                    font-size: 11px;
                                                                    font-weight: 500;
                                                                    line-height: 1.36;
                                                                "
                                                            >
                                                                <a
                                                                    href="mailto:service2@trago.com"
                                                                    style="
                                                                        text-decoration: none;
                                                                        color: #000;
                                                                    "
                                                                >
                                                                    service2@trago.com</a
                                                                >
                                                            </p>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td
                                                style="
                                                    height: 0.5px;
                                                    background-color: #335291;
                                                    padding: 0;
                                                "
                                            ></td>
                                        </tr>
                                        <tr>
                                            <td
                                                align="center"
                                                style="padding: 25px 0 23px 0"
                                            >
                                                <span
                                                    style="
                                                        font-size: 11px;
                                                        font-weight: 600;
                                                        line-height: 1.64;
                                                        text-transform: uppercase;
                                                        letter-spacing: 0.44px;
                                                        color: #179ad2;
                                                    "
                                                    >Visit
                                                    <a
                                                        href="freightgain.com"
                                                        style="
                                                            text-decoration: none;
                                                            color: #179ad2;
                                                        "
                                                        >freightgain.com</a
                                                    ></span
                                                >
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="center">
                                                <span
                                                    ><a href="#"
                                                        ><img
                                                            style="
                                                                width: 20px;
                                                                height: 20px;
                                                            "
                                                            src="http://ui.openspace.website/akshay/fg-client/img/instagram.png"
                                                            alt="Instagram" /></a
                                                ></span>
                                                <span
                                                    style="margin-left: 27.5px"
                                                    ><a href="#"
                                                        ><img
                                                            style="
                                                                width: 18.7px;
                                                                height: 18.7px;
                                                            "
                                                            src="http://ui.openspace.website/akshay/fg-client/img/facebook.png"
                                                            alt="facebook" /></a
                                                ></span>
                                                <span
                                                    style="margin-left: 27.5px"
                                                    ><a href="#"
                                                        ><img
                                                            style="
                                                                width: 23.2px;
                                                                height: 18.7px;
                                                            "
                                                            src="http://ui.openspace.website/akshay/fg-client/img/twitter.png"
                                                            alt="twitter" /></a
                                                ></span>
                                                <span
                                                    style="margin-left: 27.5px"
                                                    ><a href="#"
                                                        ><img
                                                            style="
                                                                width: 17.5px;
                                                                height: 17.5px;
                                                            "
                                                            src="http://ui.openspace.website/akshay/fg-client/img/linkedin.png"
                                                            alt="linkedin" /></a
                                                ></span>
                                                <span
                                                    style="margin-left: 27.5px"
                                                    ><a href="#"
                                                        ><img
                                                            style="
                                                                width: 28px;
                                                                height: 20px;
                                                            "
                                                            src="http://ui.openspace.website/akshay/fg-client/img/youtube.png"
                                                            alt="youtube" /></a
                                                ></span>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                        <tr>
                            <td>
                                <table
                                    width="100%"
                                    style="padding: 13px 30px 0 30px"
                                >
                                    <tr>
                                        <td align="center">
                                            <span
                                                style="
                                                    font-size: 10px;
                                                    color: #9a9a9a;
                                                    line-height: normal;
                                                "
                                                >This email was sent to you as a
                                                registered member of FrieghtGain
                                                Co. Use of the service and
                                                website is <br />
                                                subject to our
                                                <span
                                                    ><a
                                                        href="#"
                                                        style="
                                                            text-decoration: none;
                                                            color: #2475c7;
                                                        "
                                                        >Terms of Use</a
                                                    ></span
                                                >
                                                and
                                                <span style="color: #2475c7"
                                                    ><a
                                                        href="#"
                                                        style="
                                                            text-decoration: none;
                                                            color: #2475c7;
                                                        "
                                                        >Privacy Statement</a
                                                    ></span
                                                ></span
                                            >
                                        </td>
                                    </tr>
                                    <tr>
                                        <td
                                            align="center"
                                            style="padding-top: 15px"
                                        >
                                            <span
                                                style="
                                                    font-size: 10px;
                                                    color: #9a9a9a;
                                                    line-height: normal;
                                                "
                                                >2022 © FreightGain CO. All
                                                RIghts Reserved.
                                            </span>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
</html>
'''
