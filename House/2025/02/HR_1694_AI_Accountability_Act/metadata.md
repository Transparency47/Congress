# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1694?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1694
- Title: AI Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 1694
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-05-14T19:00:35Z
- Update date including text: 2025-05-14T19:00:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1694",
    "number": "1694",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "AI Accountability Act",
    "type": "HR",
    "updateDate": "2025-05-14T19:00:35Z",
    "updateDateIncludingText": "2025-05-14T19:00:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:10:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1694ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1694\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Harder of California (for himself and Ms. Kelly of Illinois ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Assistant Secretary of Commerce for Communications and Information to conduct a study and hold public meetings with respect to artificial intelligence systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Artificial Intelligence Accountability Act or the AI Accountability Act .\n#### 2. Study on accountability measures for artificial intelligence systems\n##### (a) Study\nThe Assistant Secretary of Commerce for Communications and Information shall conduct a study on accountability measures for artificial intelligence systems, which shall include an analysis of the following:\n**(1)**\nHow accountability measures are being incorporated into artificial intelligence systems used by communications networks (including telecommunications networks and social media platforms) and electromagnetic spectrum sharing applications.\n**(2)**\nHow accountability measures for artificial intelligence systems can facilitate the closing of the digital divide and assist the promotion of digital inclusion in the United States.\n**(3)**\nHow accountability measures may reduce risks related to artificial intelligence systems, including cybersecurity risks.\n**(4)**\nHow the term trustworthy is used and defined in the context of artificial intelligence, including how the term may be applied in various contexts related to artificial intelligence.\n**(5)**\nThe relationship, with respect to artificial intelligence, between the term trustworthy and other terms such as responsible and human-centric .\n##### (b) Stakeholder consultation\nIn carrying out the study required by subsection (a), the Assistant Secretary shall hold public meetings to consult with relevant stakeholders for the purpose of soliciting feedback on accountability measures for artificial intelligence systems.\n##### (c) Report\nNot later than 18 months after the date of the enactment of this Act, the Assistant Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report on the results of the study required by subsection (a) that shall include\u2014\n**(1)**\nthe results of the analysis required by subsection (a);\n**(2)**\na description of the feedback provided during the meetings required by subsection (b); and\n**(3)**\nrecommendations for governmental and nongovernmental actions to support effective accountability measures for artificial intelligence systems.\n##### (d) Accountability measure defined\nIn this section, the term accountability measure means a mechanism, including an audit, an assessment, or a certification, designed to provide assurance that a system is trustworthy.\n#### 3. Availability of information on artificial intelligence systems\n##### (a) Meetings\nThe Assistant Secretary of Commerce for Communications and Information shall hold public meetings to consult with relevant stakeholders (including representatives of industry, academia, and consumers) for the purpose of soliciting feedback on\u2014\n**(1)**\nthe information that should be available to individuals, communities, and businesses that interact with, are affected by, or study artificial intelligence systems; and\n**(2)**\nthe most effective methods for making such information available to such individuals, communities, and businesses.\n##### (b) Report\nNot later than 18 months after the date of the enactment of this Act, the Assistant Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report on the results of the meetings required by subsection (a) that shall include\u2014\n**(1)**\na description of the feedback provided during the meetings; and\n**(2)**\nrecommendations with respect to\u2014\n**(A)**\nthe information that should be available to individuals, communities, and businesses that interact with, are affected by, or study artificial intelligence systems; and\n**(B)**\nthe methods to be used for making such information available to such individuals, communities, and businesses.",
      "versionDate": "2025-02-27",
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
        "updateDate": "2025-03-19T15:12:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1694",
          "measure-number": "1694",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1694v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Artificial Intelligence Accountability Act or the AI Accountability Act</strong></p><p>This bill requires the National Telecommunications and Information Administration (NTIA) to study and report on accountability measures for artificial intelligence (AI) systems. Under the bill, accountability measures are mechanisms designed to assure that a system is trustworthy, including audits, assessments, and certifications.\u00a0</p><p>Specifically, the NTIA must study, solicit stakeholder feedback about, and report to Congress on the incorporation of accountability measures into AI systems used by communications technologies (such as telecommunications networks and social media platforms) and the ways in which AI accountability measures reduce risks related to AI systems (e.g., cybersecurity risks), among other topics.\u00a0</p><p>The NTIA must also solicit stakeholder feedback and report to Congress on (1) information that should be available to individuals, communities, and businesses that interact with, are affected by, or study AI systems; and (2) methods for making that information available.</p>"
        },
        "title": "AI Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1694.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Artificial Intelligence Accountability Act or the AI Accountability Act</strong></p><p>This bill requires the National Telecommunications and Information Administration (NTIA) to study and report on accountability measures for artificial intelligence (AI) systems. Under the bill, accountability measures are mechanisms designed to assure that a system is trustworthy, including audits, assessments, and certifications.\u00a0</p><p>Specifically, the NTIA must study, solicit stakeholder feedback about, and report to Congress on the incorporation of accountability measures into AI systems used by communications technologies (such as telecommunications networks and social media platforms) and the ways in which AI accountability measures reduce risks related to AI systems (e.g., cybersecurity risks), among other topics.\u00a0</p><p>The NTIA must also solicit stakeholder feedback and report to Congress on (1) information that should be available to individuals, communities, and businesses that interact with, are affected by, or study AI systems; and (2) methods for making that information available.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr1694"
    },
    "title": "AI Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Artificial Intelligence Accountability Act or the AI Accountability Act</strong></p><p>This bill requires the National Telecommunications and Information Administration (NTIA) to study and report on accountability measures for artificial intelligence (AI) systems. Under the bill, accountability measures are mechanisms designed to assure that a system is trustworthy, including audits, assessments, and certifications.\u00a0</p><p>Specifically, the NTIA must study, solicit stakeholder feedback about, and report to Congress on the incorporation of accountability measures into AI systems used by communications technologies (such as telecommunications networks and social media platforms) and the ways in which AI accountability measures reduce risks related to AI systems (e.g., cybersecurity risks), among other topics.\u00a0</p><p>The NTIA must also solicit stakeholder feedback and report to Congress on (1) information that should be available to individuals, communities, and businesses that interact with, are affected by, or study AI systems; and (2) methods for making that information available.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr1694"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1694ih.xml"
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
      "title": "AI Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T09:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AI Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T09:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Artificial Intelligence Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T09:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Assistant Secretary of Commerce for Communications and Information to conduct a study and hold public meetings with respect to artificial intelligence systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T09:48:27Z"
    }
  ]
}
```
