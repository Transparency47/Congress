# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1468?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1468
- Title: Protect America’s Innovation and Economic Security from CCP Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1468
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-05-27T14:20:27Z
- Update date including text: 2026-05-27T14:20:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 9.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 9.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1468",
    "number": "1468",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000589",
        "district": "5",
        "firstName": "Lance",
        "fullName": "Rep. Gooden, Lance [R-TX-5]",
        "lastName": "Gooden",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Protect America\u2019s Innovation and Economic Security from CCP Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-27T14:20:27Z",
    "updateDateIncludingText": "2026-05-27T14:20:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 9.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
        "item": [
          {
            "date": "2026-03-26T18:33:16Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-21T20:33:20Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "WI"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "UT"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TN"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "CO"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "VA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "IN"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "NE"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1468ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1468\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Gooden (for himself, Mr. Tiffany , Mr. Kennedy of Utah , Mr. Ogles , Ms. Boebert , Mr. Fallon , and Mr. Cline ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish the CCP Initiative program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect America\u2019s Innovation and Economic Security from CCP Act of 2025 .\n#### 2. CCP Initiative\n##### (a) Establishment\nThere is established in the National Security Division of the Department of Justice the CCP Initiative to\u2014\n**(1)**\ncounter nation-state threats to the United States;\n**(2)**\ncurb spying by the Chinese Communist Party on United States intellectual property and academic institutions in the United States;\n**(3)**\ndevelop an enforcement strategy concerning nontraditional collectors, including researchers in labs, universities, and the defense industrial base, that are being used to transfer technology contrary to United States interests;\n**(4)**\nimplement the Foreign Investment Risk Review Modernization Act of 2018 (title XVII of division A of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 132 Stat. 2173)) for the Department of Justice, including by working with the Department of the Treasury to develop regulations under that Act;\n**(5)**\nidentify cases under the Foreign Corrupt Practices Act of 1977 ( Public Law 95\u2013213 ; 91 Stat. 1494) involving Chinese companies that compete with United States businesses;\n**(6)**\nprioritize\u2014\n**(A)**\nidentifying and prosecuting those engaged in trade secret theft, hacking, and economic espionage;\n**(B)**\nprotecting the critical infrastructure in the United States against external threats through foreign direct investment and supply chain compromises; and\n**(C)**\nidentifying Chinese Communist Party theft of intellectual property from small businesses; and\n**(7)**\ninvestigate investments made by Chinese companies included on the Entity List maintained by the Bureau of Industry and Security of the Department of Commerce or the People\u2019s Republic of China Military Companies list maintained by the Department of Defense, and report to the Secretary of Commerce and the Secretary of Defense on any findings of such investigations, including findings related to subsidiaries or other entities controlled by such companies, whether or not such subsidiaries or other entities are registered in or operate in the People\u2019s Republic of China.\n##### (b) Consultation\nIn executing the CCP Initiative\u2019s objectives as set forth in subsection (a), the Attorney General, acting through the Assistant Attorney General for National Security, shall consult with relevant components of the Department of Justice as necessary, and coordinate activities with the Federal Bureau of Investigation and any other Federal agency as necessary.\n##### (c) Requirement\nUnder the CCP Initiative\u2014\n**(1)**\nthe Initiative shall be separate from and not under the authority or discretion of any other Department of Justice initiative dedicated to countering nation-state threats; and\n**(2)**\nall resources used for the CCP Initiative shall solely be set aside for the CCP Initiative and shall not be combined to support any other Department of Justice program, including other programs and initiatives dedicated to countering nation-state threats.\n##### (d) Annual report\nThe Attorney General shall submit annually a written report to the Committee on Homeland Security and Governmental Affairs and the Committee on the Judiciary of the Senate, and the Committee on Homeland Security and the Committee on the Judiciary of the House of Representatives, on the progress and challenges of the CCP Initiative over the preceding year, including\u2014\n**(1)**\nits progress in accomplishing the objectives set forth in subsection (a);\n**(2)**\nthe amount and sufficiency of resources provided to, and expended by, the CCP Initiative;\n**(3)**\nthe level and effectiveness of coordination with the Federal Bureau of Investigation and other Federal agencies;\n**(4)**\nthe status of efforts by and the financial intelligence capabilities of the Chinese Communist Party to engage in trade secret theft, hacking, and economic espionage;\n**(5)**\nan analysis of the use of unmanned aircraft and associated elements (including communication links and the components that control the unmanned aircraft required for the operator to operate safely and efficiently in the national airspace system) by the CCP;\n**(6)**\nthe impact of the CCP Initiative on those efforts of the Chinese Communist Party;\n**(7)**\nthe level and effectiveness of coordination and information sharing between Government agencies and private companies about economic espionage threats; and\n**(8)**\nan assessment of the economic loss to the United States as a result of hacking and trade secret theft by the Chinese Communist Party.\n##### (e) Sunset\nThis Act shall take effect on the date of enactment of this Act and cease to be in effect on the date that is 6 years after that date.\n##### (f) Severability\nIf any provision of this Act, or the application of such provision to any person or circumstance, is held to be unconstitutional, the remainder of this Act, and the application of the provisions of such to any person or circumstance, shall not be affected thereby.",
      "versionDate": "2025-02-21",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-20",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "672",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect America\u2019s Innovation and Economic Security from CCP Act of 2025",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "China",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "Department of Justice",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "Intellectual property",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "Intelligence activities, surveillance, classified information",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-08T20:32:15Z"
          },
          {
            "name": "Trade secrets and economic espionage",
            "updateDate": "2025-07-10T17:34:40Z"
          },
          {
            "name": "U.S. and foreign investments",
            "updateDate": "2025-07-10T17:34:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-18T16:23:43Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1468ih.xml"
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
      "title": "Protect America\u2019s Innovation and Economic Security from CCP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-18T04:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect America\u2019s Innovation and Economic Security from CCP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the CCP Initiative program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T04:33:31Z"
    }
  ]
}
```
