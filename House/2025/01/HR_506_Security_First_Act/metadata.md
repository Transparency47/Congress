# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/506?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/506
- Title: Security First Act
- Congress: 119
- Bill type: HR
- Bill number: 506
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-04-02T16:36:35Z
- Update date including text: 2025-04-02T16:36:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2025-01-16 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2025-01-16 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/506",
    "number": "506",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000594",
        "district": "23",
        "firstName": "Tony",
        "fullName": "Rep. Gonzales, Tony [R-TX-23]",
        "lastName": "Gonzales",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Security First Act",
    "type": "HR",
    "updateDate": "2025-04-02T16:36:35Z",
    "updateDateIncludingText": "2025-04-02T16:36:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Counterterrorism and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-01-16T14:09:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-01-16T18:46:48Z",
                "name": "Referred to"
              }
            },
            "name": "Border Security and Enforcement Subcommittee",
            "systemCode": "hshm11"
          },
          {
            "activities": {
              "item": {
                "date": "2025-01-16T18:46:48Z",
                "name": "Referred to"
              }
            },
            "name": "Counterterrorism and Intelligence Subcommittee",
            "systemCode": "hshm05"
          }
        ]
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-16T14:09:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "True",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IA"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "CO"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NJ"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IA"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "LA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "GU"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr506ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 506\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Tony Gonzales of Texas (for himself, Mr. Ciscomani , Ms. Salazar , Ms. De La Cruz , Mr. Feenstra , Mr. Evans of Colorado , Mr. Valadao , Mrs. Kim , Mr. Kean , Mr. Babin , Mr. Crenshaw , Mr. Weber of Texas , Mrs. Hinson , Mr. Higgins of Louisiana , and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Homeland Security , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require assessments for Foreign Terrorist Organization designations, authorize certain appropriations for certain fiscal years for Operation Stonegarden, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Security First Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSince FY2021, there were more than 8.72 million encounters at the Southwest border.\n**(2)**\nSince FY2021, there have been roughly 2 million known gotaways that have evaded United States Border Patrol.\n**(3)**\nSince FY2021, there were 395 encounters in between our borders with individuals on the Terrorist Screening Dataset, also known as the terrorist watchlist.\n**(4)**\nSince FY2021, 9,254 pounds of fentanyl have been seized between ports of entry nationwide.\n**(5)**\nIn 2023, there were 105,007 opioid deaths, with 72,776 deaths involving synthetic opioids like fentanyl.\n**(6)**\nMexican cartels and transnational criminal organizations have been linked to committing severe crimes including homicides, rape, sexual assault, and kidnappings, and significantly influence drug trafficking and human trafficking across the Southwest border, organizing and profiting off these illicit operations.\n**(7)**\nIn 2024, U.S. Border Patrol sent out multiple alerts to personnel warning of Mexican cartel members being permitted to shoot at Border Patrol Agents and engage in retaliatory shootings, a direct threat to homeland security.\n**(8)**\nIn 2024, Homeland Security Investigations (HSI) sent out an alert to personnel that Venezuelan gang Tren de Aragua had been given the green light to fire on or attack law enforcement in Colorado, a direct threat to homeland security.\n**(9)**\nState and local law enforcement continue to assume a larger and critical role aiding federal law enforcement in border security operations with limited, finite resources.\n**(10)**\nFederal, State, and local law enforcement need the resources necessary to secure U.S. borders and protect the homeland.\n#### 3. Operation Stonegarden appropriations and trust fund\n##### (a) Certain appropriations\nThere is authorized to be appropriated for each of fiscal years 2025 through 2028 $110,000,000 for the Operation Stonegarden grant program, and not less than $36,666,666 for each of fiscal years 2025 through 2028 to procure technology and equipment, including communications equipment, sensors, and drone technology.\n##### (b) Operation Stonegarden trust fund\n**(1) Creation of trust fund**\nThere is established in the Treasury of the United States a trust fund to be known as the Operation Stonegarden Trust Fund (referred to in this section as the Trust Fund ), consisting of amounts transferred to the Trust Fund under paragraph (2).\n**(2) Transfers to trust fund**\nThe Secretary of the Treasury shall transfer to the Trust Fund, from the general fund of the Treasury, for fiscal year 2025 and each fiscal year thereafter until 2028, an amount equivalent to the amount received into the general fund during that fiscal year attributable to unreported monetary instruments seized by U.S. Customs and Border Protection from individuals crossing the United States and Mexico border.\n**(3) Use of trust fund**\nAmounts in the Trust Fund shall be made available to the Secretary of Homeland Security, without further appropriation, to fund the Operation Stonegarden grant program.\n**(4) Limitation**\nThe Secretary may only expend funds made available from the Trust Fund to carry out the activity described in paragraph (3).\n**(5) Monetary instrument**\n**(A) In general**\nExcept as provided in subparagraph (B), a monetary instrument means\u2014\n**(i)**\ncoin or currency of the United States or of any other country;\n**(ii)**\ntraveler\u2019s checks in any form;\n**(iii)**\nnegotiable instruments, including checks, promissory notes, and money orders in bearer form, endorsed without restriction, made out to a fictitious payee, or otherwise in such form that title thereto passes upon delivery;\n**(iv)**\nincomplete instruments, including checks, promissory notes, and money orders that are signed but on which the name of the payee has been omitted; and\n**(v)**\nsecurities or stock in bearer form or otherwise in such form that title thereto passes upon delivery.\n**(B) Exception**\nA monetary instrument referred to in subparagraph (A) does not include\u2014\n**(i)**\nchecks or money orders made payable to the order of a named person which have not been endorsed or which bear restrictive endorsements;\n**(ii)**\nwarehouse receipts; or\n**(iii)**\nbills of lading.\n#### 4. Foreign terrorist organization designations\n##### (a) Report\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Secretary shall submit to the appropriate congressional committees a report on whether Mexican drug cartels and criminal gangs meet the criteria for designation as foreign terrorist organizations.\n**(2) Mexican drug cartels described**\nThe Mexican drug cartels and criminal gangs described in this paragraph are each of the following:\n**(A)**\nJalisco New Generation Cartel.\n**(B)**\nSinaloa Cartel.\n**(C)**\nJuarez Cartel.\n**(D)**\nTijuana Cartel.\n**(E)**\nGulf Cartel.\n**(F)**\nLos Zetas.\n**(3) Criminal gangs described**\nThe criminal gangs described in this paragraph refer to the Tren De Aragua.\n##### (b) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs and the Committee on Homeland Security of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations and the Committee on Homeland Security and Governmental Affairs of the Senate.\n**(2) Foreign terrorist organization**\nThe term foreign terrorist organization has the meaning given the term in section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ).\n**(3) Secretary**\nThe term Secretary means the Secretary of State.\n#### 5. Southern border technology needs analysis and updates\n##### (a) Technology needs analysis\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall submit, to the appropriate congressional committees, a technology needs analysis for border security technology along the Southwest border.\n##### (b) Contents\nThe analysis required under subsection (a) shall include an assessment of\u2014\n**(1)**\nthe technology needs and gaps along the Southwest border\u2014\n**(A)**\nto prevent terrorists and instruments of terror from entering the United States;\n**(B)**\nto combat and reduce cross-border criminal activity, including, but not limited to\u2014\n**(i)**\nthe transport of illegal goods, such as illicit drugs; and\n**(ii)**\nhuman smuggling and human trafficking; and\n**(C)**\nto facilitate the flow of legal trade across the Southwest border;\n**(2)**\nrecent technological advancements in\u2014\n**(A)**\nmanned aircraft sensor, communication, and common operating picture technology;\n**(B)**\nunmanned aerial systems and related technology, including counter-unmanned aerial system technology;\n**(C)**\nsurveillance technology, including\u2014\n**(i)**\nmobile surveillance vehicles;\n**(ii)**\nassociated electronics, including cameras, sensor technology, and radar;\n**(iii)**\ntower-based surveillance technology;\n**(iv)**\nadvanced unattended surveillance sensors; and\n**(v)**\ndeployable, lighter-than-air, ground surveillance equipment;\n**(D)**\nnonintrusive inspection technology, including non-x ray devices utilizing muon tomography and other advanced detection technology;\n**(E)**\ntunnel detection technology; and\n**(F)**\ncommunications equipment, including\u2014\n**(i)**\nradios;\n**(ii)**\nlong-term evolution broadband; and\n**(iii)**\nminiature satellites;\n**(3)**\nany other technological advancements that the Secretary determines to be critical to the Department's mission along the Southwest border;\n**(4)**\nwhether the use of the technological advances described in paragraphs (2) and (3) will\u2014\n**(A)**\nimprove border security;\n**(B)**\nimprove the capability of the Department to accomplish its mission along the Southwest border;\n**(C)**\nreduce technology gaps along the Southwest border; and\n**(D)**\nenhance the safety of any officer or agent of the Department or any other Federal agency;\n**(5)**\nthe Department's ongoing border security technology development efforts, including efforts by\u2014\n**(A)**\nU.S. Customs and Border Protection;\n**(B)**\nthe Science and Technology Directorate; and\n**(C)**\nthe technology assessment office of any other operational component;\n**(6)**\nthe technology needs for improving border security, such as\u2014\n**(A)**\ninformation technology or other computer or computing systems data capture;\n**(B)**\nbiometrics;\n**(C)**\ncloud storage; and\n**(D)**\nintelligence data sharing capabilities among agencies within the Department;\n**(7)**\nany other technological needs or factors, including border security infrastructure, such as physical barriers or dual-purpose infrastructure, that the Secretary determines should be considered; and\n**(8)**\ncurrently deployed technology or new technology that would improve the Department's ability\u2014\n**(A)**\nto reasonably achieve operational control and situational awareness along the Southwest border; and\n**(B)**\nto collect metrics for securing the border at and between ports of entry, as required under subsections (b) and (c) of section 1092 of division A of the National Defense Authorization Act for Fiscal Year 2017 ( 6 U.S.C. 223 ).\n##### (c) Updates\n**(1) In general**\nNot later than 2 years after the submission of the analysis required under subsection (a), and biannually thereafter for the following 4 years, the Secretary shall submit an update to such analysis to the appropriate congressional committees.\n**(2) Contents**\nEach update required under paragraph (1) shall include a plan for utilizing the resources of the Department to meet the border security technology needs and gaps identified pursuant to subsection (b), including developing or acquiring technologies not currently in use by the Department that would allow the Department to bridge existing border technology gaps along the Southwest border.\n##### (d) Items To be considered\nIn compiling the technology needs analysis and updates required under this section, the Secretary shall consider and examine\u2014\n**(1)**\ntechnology that is deployed and is sufficient for the Department's use along the Southwest border;\n**(2)**\ntechnology that is deployed, but is insufficient for the Department's use along the Southwest border;\n**(3)**\ntechnology that is not deployed, but is necessary for the Department's use along the Southwest border;\n**(4)**\ncurrent formal departmental requirements documentation examining current border security threats and challenges faced by any component of the Department;\n**(5)**\ntrends and forecasts regarding migration across the Southwest border;\n**(6)**\nthe impact on projected staffing and deployment needs for the Department, including staffing needs that may be fulfilled through the use of technology;\n**(7)**\nthe needs and challenges faced by employees of the Department who are deployed along the Southwest border;\n**(8)**\nthe need to improve cooperation among Federal, State, Tribal, local, and Mexican law enforcement entities to enhance security along the Southwest border;\n**(9)**\nthe privacy implications of existing technology and the acquisition and deployment of new technologies and supporting infrastructure, with an emphasis on how privacy risks might be mitigated through the use of technology, training, and policy;\n**(10)**\nthe impact of any ongoing public health emergency that impacts Department operations along the Southwest border; and\n**(11)**\nthe ability of, and the needs for, the Department to assist with search and rescue efforts for individuals or groups that may be in physical danger or in need of medical assistance.\n##### (e) Form\nTo the extent possible, the Secretary shall submit the technology needs analysis and updates required under this section in unclassified form, but may submit such documents, or portions of such documents, in classified form if the Secretary determines that such action is appropriate.\n##### (f) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(B)**\nthe Committee on Homeland Security of the House of Representatives.\n**(2) Department**\nThe term Department means the Department of Homeland Security.\n**(3) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n**(4) Southwest border**\nThe term Southwest border means the international land border between the United States and Mexico, including the ports of entry along such border.\n#### 6. Report Relating To Hiring Practices of the Department from 2018 to 2024\nNot later than 120 days after the date of enactment of this Act, the Secretary shall submit to the appropriate congressional committees a report relating the hiring practices of the Department that includes\u2014\n**(1)**\ninformation relating to the recruitment practices of the Department from 2018 to 2024; and\n**(2)**\nrecommendations with respect to improving the operational capacity of the Department workforce.",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-13T19:42:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr506",
          "measure-number": "506",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr506v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Security First Act</strong></p><p>This bill reauthorizes the Operation Stonegarden program from FY2025 through FY2028 and addresses other border security issues. (Operation Stonegarden provides grants to enhance the border security capabilities of state, local, and tribal governments.)</p><p>From FY2025 through FY2028, the money from unreported monetary instruments seized from individuals crossing the U.S.-Mexico border and transferred into the Department of the Treasury general fund shall be made available without further appropriation to the Department of Homeland Security (DHS) to fund Operation Stonegarden.</p><p>DHS must report to Congress on (1) DHS hiring practices from 2018 to 2024, and (2) whether certain criminal gangs and Mexican drug cartels meet the criteria to be designated as foreign terrorist organizations. DHS must also periodically report to Congress about the technology needed to secure the U.S.-Mexico land border.</p>"
        },
        "title": "Security First Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr506.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Security First Act</strong></p><p>This bill reauthorizes the Operation Stonegarden program from FY2025 through FY2028 and addresses other border security issues. (Operation Stonegarden provides grants to enhance the border security capabilities of state, local, and tribal governments.)</p><p>From FY2025 through FY2028, the money from unreported monetary instruments seized from individuals crossing the U.S.-Mexico border and transferred into the Department of the Treasury general fund shall be made available without further appropriation to the Department of Homeland Security (DHS) to fund Operation Stonegarden.</p><p>DHS must report to Congress on (1) DHS hiring practices from 2018 to 2024, and (2) whether certain criminal gangs and Mexican drug cartels meet the criteria to be designated as foreign terrorist organizations. DHS must also periodically report to Congress about the technology needed to secure the U.S.-Mexico land border.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr506"
    },
    "title": "Security First Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Security First Act</strong></p><p>This bill reauthorizes the Operation Stonegarden program from FY2025 through FY2028 and addresses other border security issues. (Operation Stonegarden provides grants to enhance the border security capabilities of state, local, and tribal governments.)</p><p>From FY2025 through FY2028, the money from unreported monetary instruments seized from individuals crossing the U.S.-Mexico border and transferred into the Department of the Treasury general fund shall be made available without further appropriation to the Department of Homeland Security (DHS) to fund Operation Stonegarden.</p><p>DHS must report to Congress on (1) DHS hiring practices from 2018 to 2024, and (2) whether certain criminal gangs and Mexican drug cartels meet the criteria to be designated as foreign terrorist organizations. DHS must also periodically report to Congress about the technology needed to secure the U.S.-Mexico land border.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr506"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr506ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Security First Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Security First Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require assessments for Foreign Terrorist Organization designations, authorize certain appropriations for certain fiscal years for Operation Stonegarden, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T05:18:20Z"
    }
  ]
}
```
