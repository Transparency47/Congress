# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2585?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2585
- Title: MAP for Broadband Funding Act
- Congress: 119
- Bill type: S
- Bill number: 2585
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2026-05-29T18:26:22Z
- Update date including text: 2026-05-29T18:26:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-11 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-121.
- 2026-05-11 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-121.
- 2026-05-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 407.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-11 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-121.
- 2026-05-11 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-121.
- 2026-05-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 407.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2585",
    "number": "2585",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "MAP for Broadband Funding Act",
    "type": "S",
    "updateDate": "2026-05-29T18:26:22Z",
    "updateDateIncludingText": "2026-05-29T18:26:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 407.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-121.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-121.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2026-05-11T22:58:59Z",
            "name": "Reported By"
          },
          {
            "date": "2026-02-12T15:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-31T17:54:17Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2585is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2585\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mrs. Fischer (for herself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo modernize and improve the Broadband Funding Map in order to promote the most efficient use of Federal funds for broadband deployment, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modernization, Accountability, and Planning for Broadband Funding Act or the MAP for Broadband Funding Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate ; and\n**(B)**\nthe Committee on Energy and Commerce of the House of Representatives .\n**(2) Broadband Funding Map**\nThe term Broadband Funding Map means the Deployment Locations Map, as defined in section 60105(a) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704(a) ).\n**(3) Broadband infrastructure**\nThe term broadband infrastructure has the meaning given that term in section 60105(a) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704(a) ).\n**(4) Commission**\nThe term Commission means the Federal Communications Commission.\n**(5) NTIA**\nThe term NTIA means the National Telecommunications and Information Administration.\n#### 3. Broadband Funding Map modernization\n##### (a) In general\nThe Commission, in coordination with NTIA, shall collect data submitted for the Broadband Funding Map by relevant Federal agencies on a reasonable and timely basis pursuant to section 60105(d) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ), in order to promote the most efficient use of Federal funds for broadband deployment and prevent redundant overbuilding of broadband infrastructure with Federal funding.\n##### (b) Inquiry\n**(1) Notice of inquiry**\nNot later than 270 days after the date of enactment of this Act, the Commission shall initiate a notice of inquiry concerning the optimum functionality and transparency of the Broadband Funding Map, including the quality and completeness of the data populated to the Broadband Funding Map.\n**(2) Evaluation considerations**\nIn the inquiry, the Commission shall include evaluation of the following considerations:\n**(A)**\nThe adequacy with which Federal agencies have been able to collect and submit the required categories of data pursuant to section 60105(d) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ) to date.\n**(B)**\nThe usability of such existing categories of data described in subparagraph (A) to the public, and whether any category should be added, eliminated, or otherwise altered for improved user experience.\n**(C)**\nThe timeliness of periodic updates from Federal agencies to the Broadband Funding Map described in subparagraph (A) pursuant to section 60105(e) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ).\n**(D)**\nWhether the scope of programmatic data to be reported to the Broadband Funding Map pursuant to section 60105(d)(1) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ) should be expanded.\n**(E)**\nAny manners in which the Commission should potentially augment or streamline the Broadband Funding Map with existing Commission mapping tools.\n**(3) Completion**\nNot later than 120 days after the initiation of the inquiry under paragraph (1), the Commission shall complete the inquiry.\n#### 4. GAO Study and Report\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Comptroller of the United States shall\u2014\n**(1)**\nconduct a study on the roles, responsibilities, and progress to date of Federal agencies to maintain the Broadband Funding Map and ensure the completeness and continued relevance of the Broadband Funding Map; and\n**(2)**\nsubmit to the appropriate congressional committees a report on the study under paragraph (1) that includes the findings and conclusions of the Comptroller General.\n##### (b) Requirements\nIn conducting the study required under subsection (a), the Comptroller General shall review the following:\n**(1)**\nThe extent to which each eligible Federal agency is submitting programmatic data to the Broadband Funding Map adequately and in compliance with section 60105 of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ), including identification of any\u2014\n**(A)**\nsuccessful best practices in submitting such data to the Commission; and\n**(B)**\nchallenges resulting in incomplete data submissions from an agency or individual program to the Commission.\n**(2)**\nThe proficiency of the Commission\u2019s management of the Broadband Funding Map and related interagency collaboration.\n**(3)**\nWhether the Commission has sufficient authority to collect the necessary data from Federal agencies to populate the Broadband Funding Map.\n**(4)**\nThe respective data collection efforts of NTIA pursuant to the ACCESS BROADBAND Act ( 47 U.S.C. 1307 ) and section 60105 of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ).\n**(5)**\nThe effectiveness of coordination among the Commission, NTIA, and other relevant Federal agencies that provide funding for broadband infrastructure deployment, including the Department of Agriculture, the Department of Health and Human Services, the Department of the Treasury, the Department of Housing and Urban Development, and the Institute of Museum and Library Sciences, pursuant to section 60105(g) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ).\n**(6)**\nHow enhanced use of the Broadband Funding Map across relevant Federal agencies could improve taxpayer savings.",
      "versionDate": "2025-07-31",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2585rs.xml",
      "text": "II\nCalendar No. 407\n119th CONGRESS\n2d Session\nS. 2585\n[Report No. 119\u2013121]\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mrs. Fischer (for herself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nMay 11, 2026 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo modernize and improve the Broadband Funding Map in order to promote the most efficient use of Federal funds for broadband deployment, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modernization, Accountability, and Planning for Broadband Funding Act or the MAP for Broadband Funding Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate ; and\n**(B)**\nthe Committee on Energy and Commerce of the House of Representatives .\n**(2) Broadband Funding Map**\nThe term Broadband Funding Map means the Deployment Locations Map, as defined in section 60105(a) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704(a) ).\n**(3) Broadband infrastructure**\nThe term broadband infrastructure has the meaning given that term in section 60105(a) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704(a) ).\n**(4) Commission**\nThe term Commission means the Federal Communications Commission.\n**(5) NTIA**\nThe term NTIA means the National Telecommunications and Information Administration.\n#### 3. Broadband Funding Map modernization\n##### (a) In general\nThe Commission, in coordination with NTIA, shall collect data submitted for the Broadband Funding Map by relevant Federal agencies on a reasonable and timely basis pursuant to section 60105(d) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ), in order to promote the most efficient use of Federal funds for broadband deployment and prevent redundant overbuilding of broadband infrastructure with Federal funding.\n##### (b) Inquiry\n**(1) Notice of inquiry**\nNot later than 270 days after the date of enactment of this Act, the Commission shall initiate a notice of inquiry concerning the optimum functionality and transparency of the Broadband Funding Map, including the quality and completeness of the data populated to the Broadband Funding Map.\n**(2) Evaluation considerations**\nIn the inquiry, the Commission shall include evaluation of the following considerations:\n**(A)**\nThe adequacy with which Federal agencies have been able to collect and submit the required categories of data pursuant to section 60105(d) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ) to date.\n**(B)**\nThe usability of such existing categories of data described in subparagraph (A) to the public, and whether any category should be added, eliminated, or otherwise altered for improved user experience.\n**(C)**\nThe timeliness of periodic updates from Federal agencies to the Broadband Funding Map described in subparagraph (A) pursuant to section 60105(e) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ).\n**(D)**\nWhether the scope of programmatic data to be reported to the Broadband Funding Map pursuant to section 60105(d)(1) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ) should be expanded.\n**(E)**\nAny manners in which the Commission should potentially augment or streamline the Broadband Funding Map with existing Commission mapping tools.\n**(3) Completion**\nNot later than 120 days after the initiation of the inquiry under paragraph (1), the Commission shall complete the inquiry.\n#### 4. GAO Study and Report\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Comptroller of the United States shall\u2014\n**(1)**\nconduct a study on the roles, responsibilities, and progress to date of Federal agencies to maintain the Broadband Funding Map and ensure the completeness and continued relevance of the Broadband Funding Map; and\n**(2)**\nsubmit to the appropriate congressional committees a report on the study under paragraph (1) that includes the findings and conclusions of the Comptroller General.\n##### (b) Requirements\nIn conducting the study required under subsection (a), the Comptroller General shall review the following:\n**(1)**\nThe extent to which each eligible Federal agency is submitting programmatic data to the Broadband Funding Map adequately and in compliance with section 60105 of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ), including identification of any\u2014\n**(A)**\nsuccessful best practices in submitting such data to the Commission; and\n**(B)**\nchallenges resulting in incomplete data submissions from an agency or individual program to the Commission.\n**(2)**\nThe proficiency of the Commission\u2019s management of the Broadband Funding Map and related interagency collaboration.\n**(3)**\nWhether the Commission has sufficient authority to collect the necessary data from Federal agencies to populate the Broadband Funding Map.\n**(4)**\nThe respective data collection efforts of NTIA pursuant to the ACCESS BROADBAND Act ( 47 U.S.C. 1307 ) and section 60105 of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ).\n**(5)**\nThe effectiveness of coordination among the Commission, NTIA, and other relevant Federal agencies that provide funding for broadband infrastructure deployment, including the Department of Agriculture, the Department of Health and Human Services, the Department of the Treasury, the Department of Housing and Urban Development, and the Institute of Museum and Library Sciences, pursuant to section 60105(g) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704 ).\n**(6)**\nHow enhanced use of the Broadband Funding Map across relevant Federal agencies could improve taxpayer savings.",
      "versionDate": "2026-05-11",
      "versionType": "Reported in Senate"
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
            "name": "Congressional oversight",
            "updateDate": "2026-02-17T19:20:30Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-02-17T19:20:24Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-02-17T19:20:17Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-02-17T19:19:08Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-02-17T19:19:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-18T19:53:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-31",
    "originChamber": "Senate",
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
          "measure-id": "id119s2585",
          "measure-number": "2585",
          "measure-type": "s",
          "orig-publish-date": "2025-07-31",
          "originChamber": "SENATE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2585v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-07-31",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Modernization, Accountability, and Planning for Broadband Funding Act or the MAP for Broadband Funding Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to coordinate with the National Telecommunications and Information Administration to collect data for the Broadband Funding Map on a reasonable and timely basis. It also requires information collection and reporting on the map\u2019s functionality and management. (The map documents the location of each federally funded broadband project.)</p><p>Specifically, the FCC must seek public comment on the functionality and transparency of the map and the quality and completeness of the data within the map. Further, the Government Accountability Office must report on the management and use of the map, as well as the extent to which federal agencies are complying with obligations to submit information for the map.</p>"
        },
        "title": "MAP for Broadband Funding Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2585.xml",
    "summary": {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Modernization, Accountability, and Planning for Broadband Funding Act or the MAP for Broadband Funding Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to coordinate with the National Telecommunications and Information Administration to collect data for the Broadband Funding Map on a reasonable and timely basis. It also requires information collection and reporting on the map\u2019s functionality and management. (The map documents the location of each federally funded broadband project.)</p><p>Specifically, the FCC must seek public comment on the functionality and transparency of the map and the quality and completeness of the data within the map. Further, the Government Accountability Office must report on the management and use of the map, as well as the extent to which federal agencies are complying with obligations to submit information for the map.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119s2585"
    },
    "title": "MAP for Broadband Funding Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Modernization, Accountability, and Planning for Broadband Funding Act or the MAP for Broadband Funding Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to coordinate with the National Telecommunications and Information Administration to collect data for the Broadband Funding Map on a reasonable and timely basis. It also requires information collection and reporting on the map\u2019s functionality and management. (The map documents the location of each federally funded broadband project.)</p><p>Specifically, the FCC must seek public comment on the functionality and transparency of the map and the quality and completeness of the data within the map. Further, the Government Accountability Office must report on the management and use of the map, as well as the extent to which federal agencies are complying with obligations to submit information for the map.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119s2585"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2585is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2585rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "MAP for Broadband Funding Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-13T04:23:32Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Modernization, Accountability, and Planning for Broadband Funding Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-13T04:23:32Z"
    },
    {
      "title": "MAP for Broadband Funding Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MAP for Broadband Funding Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Modernization, Accountability, and Planning for Broadband Funding Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modernize and improve the Broadband Funding Map in order to promote the most efficient use of Federal funds for broadband deployment, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:37Z"
    }
  ]
}
```
