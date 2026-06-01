# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/644?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/644
- Title: Modernizing Retrospective Regulatory Review Act
- Congress: 119
- Bill type: S
- Bill number: 644
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-09-09T15:31:52Z
- Update date including text: 2025-09-09T15:31:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/644",
    "number": "644",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Modernizing Retrospective Regulatory Review Act",
    "type": "S",
    "updateDate": "2025-09-09T15:31:52Z",
    "updateDateIncludingText": "2025-09-09T15:31:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
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
        "item": {
          "date": "2025-02-20T15:43:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s644is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 644\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Lee (for himself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo improve retrospective reviews of Federal regulations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modernizing Retrospective Regulatory Review Act .\n#### 2. Improving retrospective reviews of Federal regulations\n##### (a) Definitions\nIn this section:\n**(1) Administrative Committee of the Federal Register**\nThe term Administrative Committee of the Federal Register means the committee established under section 1506 of title 44, United States Code.\n**(2) Administrator**\nThe term Administrator means the Administrator of the Office of Information and Regulatory Affairs.\n**(3) Agency**\nThe term agency has the meaning given the term in section 3502 of title 44, United States Code.\n**(4) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Oversight and Government Reform of the House of Representatives; and\n**(B)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate.\n**(5) Director of GPO**\nThe term Director of GPO means the Director of the Government Publishing Office.\n**(6) Machine-readable**\nThe term machine-readable has the meaning given the term in section 3502 of title 44, United States Code.\n**(7) Retrospective review of a regulation of the agency**\nThe term retrospective review of a regulation of the agency means a review of regulations of the agency conducted after the regulation has been issued that is required by law or determined appropriate by the head of the agency.\n##### (b) Report on availability of existing regulations in machine-Readable format\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Director of the Office of Management and Budget, acting through the Administrator and in consultation with the Director of GPO, the Archivist of the United States, and the Director of the Federal Register, shall submit to the appropriate congressional committees, a report on the progress of the Federal Government in making regulations of agencies available in machine-readable format.\n**(2) Contents of report**\nThe report required by paragraph (1) shall include\u2014\n**(A)**\nan assessment of whether agency regulations have been made available in a machine-readable format to the public; and\n**(B)**\ninformation regarding the recognition by the Administrative Committee of the Federal Register of the eCFR maintained by the Director of the Federal Register and the Director of GPO as an official legal edition of the Code of Federal Regulations.\n##### (c) Guidance on using technology to conduct retrospective reviews\n**(1) In general**\nNot later than 18 months after the date of enactment of this Act, the Director of the Office of Management and Budget, acting through the Administrator, shall issue guidance on how the head of an agency can\u2014\n**(A)**\nuse technology (including algorithmic tools and artificial intelligence) to more efficiently, cost-effectively, and accurately conduct any retrospective review of the existing regulations of the agency, including how to identify, procure, and use such technology to identify through any such review regulations of the agency that\u2014\n**(i)**\nare obsolete, ineffective, or insufficient;\n**(ii)**\nare excessively burdensome or should be improved;\n**(iii)**\ncontain typographical errors;\n**(iv)**\ncontain inaccurate cross references; or\n**(v)**\nare redundant, contradict, or overlap with any regulations or standards of the agency; and\n**(B)**\nadequately train personnel of the agency on how to use such technology.\n**(2) Development of guidance**\nIn developing the guidance required pursuant to paragraph (1), the Administrator shall take into account any assessment or information included in the report required by subsection (b).\n##### (d) Agency retrospective review plan\nNot later than 2 years after the date of enactment of this Act, the head of each agency shall submit to the Administrator and the appropriate congressional committees a plan that\u2014\n**(1)**\nincludes a detailed strategy for implementing the guidance issued pursuant to subsection (c) with respect to the regulations of the agency;\n**(2)**\nidentifies any regulation of the agency, or categories of regulations of the agency, that the head of the agency\u2014\n**(A)**\nis required by law to review after the applicable regulation is issued; or\n**(B)**\ndetermines would benefit from being reviewed after the regulation is issued; and\n**(3)**\nincludes any additional information, data, or ex-post analysis determined necessary or useful by the head of the agency.\n##### (e) Agency implementation\nNot later than 180 days after the date on which the head of an agency submits the plan required by subsection (d), the head of the agency shall implement the strategy included in such plan with respect to any retrospective review of a regulation of the agency.",
      "versionDate": "2025-02-20",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-05-21",
        "text": "Ordered to be Reported by the Yeas and Nays: 24 - 18."
      },
      "number": "67",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Modernizing Retrospective Regulatory Review",
      "type": "HR"
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-07-10T14:36:42Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-07-10T14:36:42Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-10T14:36:42Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-10T14:36:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-06T20:52:55Z"
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
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s644is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Modernizing Retrospective Regulatory Review Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Modernizing Retrospective Regulatory Review Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve retrospective reviews of Federal regulations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T03:18:28Z"
    }
  ]
}
```
