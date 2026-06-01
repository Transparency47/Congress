# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3510?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3510
- Title: Biosimilar Inspection Modernization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3510
- Origin chamber: Senate
- Introduced date: 2025-12-16
- Update date: 2026-01-12T16:41:05Z
- Update date including text: 2026-01-12T16:41:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in Senate
- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-16: Introduced in Senate

## Actions

- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3510",
    "number": "3510",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Biosimilar Inspection Modernization Act of 2025",
    "type": "S",
    "updateDate": "2026-01-12T16:41:05Z",
    "updateDateIncludingText": "2026-01-12T16:41:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T22:30:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3510is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3510\nIN THE SENATE OF THE UNITED STATES\nDecember 16, 2025 Mr. Budd (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo improve the inspections of drug establishments engaged in the manufacture, preparation, propagation, or processing of biosimilar biological products conducted by the Food and Drug Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Biosimilar Inspection Modernization Act of 2025 .\n#### 2. Definitions\nIn this Act\u2014\n**(1)**\nthe term biosimilar biological product means a biological product licensed under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) );\n**(2)**\nthe term biosimilar biological product establishment means an establishment engaged in the manufacture, preparation, propagation, or processing of a biosimilar biological product and registered under subsection (b)(1), (c)(1), or (i) of section 510 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360 ); and\n**(3)**\nthe term Secretary means the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs.\n#### 3. Public meeting and report on mutual recognition agreements\n##### (a) Public meeting\nNot later than 180 days after the date of enactment of this Act, the Secretary shall conduct a public meeting on the use of mutual recognition agreements for purposes of carrying out inspections under section 704 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 374 ) of establishments engaged in the manufacture, preparation, propagation, or processing of a biosimilar biological product, including a discussion of\u2014\n**(1)**\nhow mutual recognition agreements are utilized with respect to the inspection of biosimilar biological product establishments, and areas for improvements in such inspections conducted pursuant to such agreements; and\n**(2)**\nareas in which use of mutual recognition agreements could be expanded to apply beyond compliance inspections under section 704 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 374 ), including for use in conjunction with remote regulatory assessments, inspections conducted by trusted foreign partners identified by the Food and Drug Administration, and virtual interactions with subject matter experts.\n##### (b) Report\nNot later than 180 days after the public meeting under subsection (a) is conducted, the Secretary shall issue to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives, and make publicly available, a report that includes recommendations on the use of mutual recognition agreements for purposes of conducting inspections of biosimilar biological product establishments.\n#### 4. Ensuring flexibility in inspection tools\nThe Secretary shall update inspection processes and existing tools to advance a risk-based approach to evaluate, including conducting inspections, of establishments engaged in the manufacture, preparation, propagation, or processing of biosimilar biological products to enable the Food and Drug Administration to\u2014\n**(1)**\nincrease utilization of remote regulatory assessments under section 704 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 374 ), in accordance with the guidance issued by the Food and Drug Administration, titled Conducting Remote Regulatory Assessments\u2014Questions and Answers (June 24, 2025) (or any successor guidance); and\n**(2)**\nmaximize the use of alternative tools set forth in the guidance described in paragraph (1) to improve inspection efficiency.\n#### 5. FDA strategic plan on domestic inspection improvements for biosimilar biological facilities\nNot later than 1 year after the date of enactment of this Act, the Secretary shall develop and publish a strategic plan on ways the Food and Drug Administration will address challenges with respect to the inspection of domestic biosimilar biological product establishments, including regarding\u2014\n**(1)**\nrecruiting and retaining inspections staff;\n**(2)**\nchallenges specific to inspecting domestic biosimilar biological product establishments;\n**(3)**\nimproving internal communication among all Food and Drug Administration personnel involved in inspections of biosimilar biological product establishments; and\n**(4)**\nexpanding opportunities for external communications with sponsors of applications under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ), including informing such sponsors about potential inspection requirements and resolving outstanding inspection related questions earlier in the review process.",
      "versionDate": "2025-12-16",
      "versionType": "Introduced in Senate"
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
        "name": "Health",
        "updateDate": "2026-01-12T16:41:04Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3510is.xml"
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
      "title": "Biosimilar Inspection Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-10T09:09:07Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Biosimilar Inspection Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-10T09:09:05Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the inspections of drug establishments engaged in the manufacture, preparation, propagation, or processing of biosimilar biological products conducted by the Food and Drug Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-10T09:03:21Z"
    }
  ]
}
```
