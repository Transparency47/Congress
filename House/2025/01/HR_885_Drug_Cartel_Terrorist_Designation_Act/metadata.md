# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/885?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/885
- Title: Drug Cartel Terrorist Designation Act
- Congress: 119
- Bill type: HR
- Bill number: 885
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-03-25T08:06:17Z
- Update date including text: 2026-03-25T08:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/885",
    "number": "885",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Drug Cartel Terrorist Designation Act",
    "type": "HR",
    "updateDate": "2026-03-25T08:06:17Z",
    "updateDateIncludingText": "2026-03-25T08:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:04:25Z",
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
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "MT"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "LA"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "OK"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TN"
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
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "WI"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "ID"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "IL"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "NC"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "CO"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "WI"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "TX"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "FL"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "AL"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr885ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 885\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Roy (for himself, Mr. Zinke , Mr. Biggs of Arizona , Mr. Cloud , Mr. Higgins of Louisiana , Mr. Fallon , Mr. Brecheen , Mr. Gosar , Mr. Arrington , Mr. Ogles , Mr. Weber of Texas , Mr. Donalds , Ms. Van Duyne , Mr. Self , and Mr. Williams of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Secretary of State to submit to Congress a report on the designation of the Gulf Cartel, the Cartel Del Noreste, the Cartel de Sinaloa, and the Cartel de Jalisco Nueva Generacion as foreign terrorist organizations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drug Cartel Terrorist Designation Act .\n#### 2. Report on designation of certain drug cartels as foreign terrorist organizations\n##### (a) Sense of Congress\nIt is the sense of Congress that each of the drug cartels set forth in subsection (b) meets the criteria for designation as a foreign terrorist organization as set forth in section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ).\n##### (b) Designation\nThe Secretary of State shall designate each of the following Mexican drug cartels as a foreign terrorist organization under such section 219:\n**(1)**\nThe Gulf Cartel.\n**(2)**\nThe Cartel Del Noreste.\n**(3)**\nThe Cartel de Sinaloa.\n**(4)**\nThe Cartel de Jalisco Nueva Generacion.\n##### (c) Report\n**(1) Report required**\nNot later than 30 days after the date of the enactment of this Act, the Secretary of State, in consultation with the Director of National Intelligence, shall submit to the appropriate committees of Congress\u2014\n**(A)**\na detailed report on each of the drug cartels listed in subsection (b) and any other cartels the Secretary may identify, including the criteria met for designation as a foreign terrorist organization as set forth in section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ); and\n**(B)**\nfor each of the cartels designated under subsection (b), if the Secretary determines that the drug cartel does not meet the criteria set forth under such section 219, a detailed justification as to which criteria have not been met.\n**(2) Designation of additional cartels**\nNot later than 30 days after the submission of the report the Secretary shall designate any cartel or any faction thereof as a foreign terrorist organization listed in the report that met the criteria for designation as a foreign terrorist organization as set forth in section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ).\n**(3) Form**\nThe report required by paragraph (1) shall\u2014\n**(A)**\nbe submitted in unclassified form, but may include a classified annex; and\n**(B)**\nbe made available only in electronic form and shall not be printed, except if a printed copy is requested by an office of the legislative branch.\n**(4) Appropriate committees of Congress defined**\nIn this subsection, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Armed Services, the Committee on Financial Services, the Committee on Foreign Affairs, the Committee on the Judiciary, the Committee on Homeland Security, and the Permanent Select Committee on Intelligence of the House of Representatives; and\n**(B)**\nthe Committee on Armed Services, the Committee on Banking, Housing, and Urban Affairs, the Committee on Foreign Relations, the Committee on the Judiciary, the Committee on Homeland Security and Governmental Affairs, and the Select Committee on Intelligence of the Senate.\n##### (d) Rule of construction\nNothing in this Act may be construed to expand the eligibility for asylum of any alien by reason of the designation of a drug cartel as a foreign terrorist organization.",
      "versionDate": "2025-01-31",
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
        "name": "International Affairs",
        "updateDate": "2025-03-04T17:29:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr885",
          "measure-number": "885",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr885v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Drug Cartel Terrorist Designation Act</strong></p><p>This bill directs the Department of State to designate four specified drug cartels as foreign terrorist organizations. (Among other things, such a designation allows the Department of the Treasury to require U.S. financial institutions to block transactions involving the organization.)</p><p>The four specified cartels in the bill are the Gulf Cartel, the Cartel Del Noreste, the Cartel de Sinaloa, and the Cartel de Jalisco Nueva Generacion.</p><p>The bill also requires the State Department to submit a detailed report on those four cartels and any other cartels it may identify. Based on this report, the State Department must designate as a foreign terrorist organization any such identified cartel (or faction thereof) that meets certain criteria for designation as a foreign terrorist organization.</p><p>The bill specifies that it may not be construed to expand eligibility for asylum.</p>"
        },
        "title": "Drug Cartel Terrorist Designation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr885.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Drug Cartel Terrorist Designation Act</strong></p><p>This bill directs the Department of State to designate four specified drug cartels as foreign terrorist organizations. (Among other things, such a designation allows the Department of the Treasury to require U.S. financial institutions to block transactions involving the organization.)</p><p>The four specified cartels in the bill are the Gulf Cartel, the Cartel Del Noreste, the Cartel de Sinaloa, and the Cartel de Jalisco Nueva Generacion.</p><p>The bill also requires the State Department to submit a detailed report on those four cartels and any other cartels it may identify. Based on this report, the State Department must designate as a foreign terrorist organization any such identified cartel (or faction thereof) that meets certain criteria for designation as a foreign terrorist organization.</p><p>The bill specifies that it may not be construed to expand eligibility for asylum.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr885"
    },
    "title": "Drug Cartel Terrorist Designation Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Drug Cartel Terrorist Designation Act</strong></p><p>This bill directs the Department of State to designate four specified drug cartels as foreign terrorist organizations. (Among other things, such a designation allows the Department of the Treasury to require U.S. financial institutions to block transactions involving the organization.)</p><p>The four specified cartels in the bill are the Gulf Cartel, the Cartel Del Noreste, the Cartel de Sinaloa, and the Cartel de Jalisco Nueva Generacion.</p><p>The bill also requires the State Department to submit a detailed report on those four cartels and any other cartels it may identify. Based on this report, the State Department must designate as a foreign terrorist organization any such identified cartel (or faction thereof) that meets certain criteria for designation as a foreign terrorist organization.</p><p>The bill specifies that it may not be construed to expand eligibility for asylum.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr885"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr885ih.xml"
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
      "title": "Drug Cartel Terrorist Designation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Drug Cartel Terrorist Designation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of State to submit to Congress a report on the designation of the Gulf Cartel, the Cartel Del Noreste, the Cartel de Sinaloa, and the Cartel de Jalisco Nueva Generacion as foreign terrorist organizations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:37Z"
    }
  ]
}
```
