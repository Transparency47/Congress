# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/477?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/477
- Title: MACH Act
- Congress: 119
- Bill type: HR
- Bill number: 477
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-01-13T09:05:36Z
- Update date including text: 2026-01-13T09:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/477",
    "number": "477",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000480",
        "district": "20",
        "firstName": "Vince",
        "fullName": "Rep. Fong, Vince [R-CA-20]",
        "lastName": "Fong",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "MACH Act",
    "type": "HR",
    "updateDate": "2026-01-13T09:05:36Z",
    "updateDateIncludingText": "2026-01-13T09:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
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
          "date": "2025-01-16T14:09:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "VA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "GA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "FL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "DE"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "NC"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "AK"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "NC"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr477ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 477\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Fong (for himself and Mr. Mullin ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo advance scientific research and technology development of hypersonic vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Making Advancements in Commercial Hypersonics Act or the MACH Act .\n#### 2. Making advancements in commercial hypersonics program\n##### (a) In general\nIn conducting hypersonics research pursuant to section 40112(d) of title 51, United States Code, the Administrator of the National Aeronautics and Space Administration (in this section referred to as the Administrator ) may establish the Making Advancements in Commercial Hypersonics Program (in this section referred to as the Program ) to facilitate opportunities for testing of high-speed aircraft and other technologies that advance scientific research and technology development related to hypersonic aircraft.\n##### (b) Limitation\nThe Program may not fund the development of technologies that are supported by the testing described in subsection (a).\n##### (c) Strategic plan\nNot later than 60 days after the date of the enactment of this Act, the Administrator, acting through the Aeronautics Research Mission Directorate, shall develop a strategic plan for activities under subsection (a) that aligns with the hypersonic research roadmap required under section 603 of the National Aeronautics and Space Administration Transition Authorization Act of 2017 ( Public Law 115\u201310 ; 51 U.S.C. 20302 note).\n##### (d) Coordination, consultation, and collaboration\n**(1) Coordination**\nThe Administrator shall ensure coordination between the Aeronautics Research Mission Directorate and other Mission Directorates, as appropriate, to identify technologies eligible for testing opportunities under the Program.\n**(2) Consultation; collaboration**\nThe Administrator shall consult and seek to collaborate, as appropriate, with the Secretary of Defense and the Administrator of the Federal Aviation Administration on activities related to the Program, including development, testing, and evaluation of high-speed aircraft and related technologies.\n##### (e) Report\nThe Administrator shall submit to the Committee on Science, Space, and Technology and the Committee on Armed Services of the House of Representatives and the Committee on Commerce, Science, and Transportation and the Committee on Armed Services of the Senate\u2014\n**(1)**\nnot later than 90 days after the date of the enactment of this Act, a report that\u2014\n**(A)**\ndescribes activities of the Program; and\n**(B)**\nincludes the strategic plan required under subsection (c); and\n**(2)**\nnot later than one year after the date of the enactment of this Act and annually thereafter, a report describing progress in carrying out the Program, including regarding the number and type of testing opportunities carried out in the previous fiscal year and planned for the upcoming fiscal year.\n##### (f) Research security\nNothing in this section authorizes the Administrator to develop, implement, or execute an agreement related to technologies under this section with any entity of concern, a foreign business entity, or a foreign country of concern.\n##### (g) Definitions\nIn this section\u2014\n**(1) Entity of concern**\nThe term entity of concern has the meaning given such term in section 10114 of the Research and Development, Competition, and Innovation Act ( Public Law 117\u2013167 ; 42 U.S.C. 18912 ).\n**(2) Foreign business entity**\nThe term foreign business entity means an entity that is majority-owned or majority-controlled (as such term is defined in section 800.208 of title 31, Code of Federal Regulations, or a successor regulation), or minority owned greater than 25 percent by\u2014\n**(A)**\nany governmental organization of a foreign country of concern; or\n**(B)**\nany other entity that is\u2014\n**(i)**\nknown to be owned or controlled by any governmental organization of a foreign country of concern; or\n**(ii)**\norganized under, or otherwise subject to, the laws of a foreign country of concern.\n**(3) Foreign country of concern**\nThe term foreign country of concern has the meaning given such term in section 9901 of title XCIX of division H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651 ).\n**(4) High-speed aircraft**\nThe term high-speed aircraft has the meaning given such term in section 1009 of the Federal Aviation Reauthorization Act of 2024 ( Public Law 118\u201363 ; 49 U.S.C. 44701 note).",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-02-14T12:41:15Z"
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
          "measure-id": "id119hr477",
          "measure-number": "477",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr477v00",
            "update-date": "2025-03-14"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Making Advancements in Commercial Hypersonics Act or the MACH Act</strong></p><p>This bill permits the National Aeronautics and Space Administration (NASA) to establish a research program to facilitate the testing of high-speed aircraft and related technologies, to be known as the Making Advancements in Commercial Hypersonics Program.</p><p>Within a specified time period, NASA must develop a strategic plan for such research. NASA must also consult with the Department of Defense and the Federal Aviation Administration on these efforts.\u00a0</p><p>Under the program, NASA may not (1) fund the development of hypersonic and related technologies; or (2) enter into an agreement with certain foreign entities of concern, including entities owned or controlled by China, Iran, North Korea, or Russia.\u00a0</p>"
        },
        "title": "MACH Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr477.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Making Advancements in Commercial Hypersonics Act or the MACH Act</strong></p><p>This bill permits the National Aeronautics and Space Administration (NASA) to establish a research program to facilitate the testing of high-speed aircraft and related technologies, to be known as the Making Advancements in Commercial Hypersonics Program.</p><p>Within a specified time period, NASA must develop a strategic plan for such research. NASA must also consult with the Department of Defense and the Federal Aviation Administration on these efforts.\u00a0</p><p>Under the program, NASA may not (1) fund the development of hypersonic and related technologies; or (2) enter into an agreement with certain foreign entities of concern, including entities owned or controlled by China, Iran, North Korea, or Russia.\u00a0</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hr477"
    },
    "title": "MACH Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Making Advancements in Commercial Hypersonics Act or the MACH Act</strong></p><p>This bill permits the National Aeronautics and Space Administration (NASA) to establish a research program to facilitate the testing of high-speed aircraft and related technologies, to be known as the Making Advancements in Commercial Hypersonics Program.</p><p>Within a specified time period, NASA must develop a strategic plan for such research. NASA must also consult with the Department of Defense and the Federal Aviation Administration on these efforts.\u00a0</p><p>Under the program, NASA may not (1) fund the development of hypersonic and related technologies; or (2) enter into an agreement with certain foreign entities of concern, including entities owned or controlled by China, Iran, North Korea, or Russia.\u00a0</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hr477"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr477ih.xml"
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
      "title": "MACH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T10:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MACH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T10:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Making Advancements in Commercial Hypersonics Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T10:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To advance scientific research and technology development of hypersonic vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T10:48:17Z"
    }
  ]
}
```
