# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1387?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1387
- Title: COST Act
- Congress: 119
- Bill type: HR
- Bill number: 1387
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2026-03-30T22:57:53Z
- Update date including text: 2026-03-30T22:57:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1387",
    "number": "1387",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "N000190",
        "district": "5",
        "firstName": "Ralph",
        "fullName": "Rep. Norman, Ralph [R-SC-5]",
        "lastName": "Norman",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "COST Act",
    "type": "HR",
    "updateDate": "2026-03-30T22:57:53Z",
    "updateDateIncludingText": "2026-03-30T22:57:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:33:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
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
      "sponsorshipDate": "2025-02-14",
      "state": "TX"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1387ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1387\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Norman (for himself, Mr. Weber of Texas , and Mr. Self ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the disclosure of information relating to the cost of programs, projects, or activities carried out using Federal funds.\n#### 1. Short title\nThis Act may be cited as the Cost Openness and Spending Transparency Act of 2025 or the COST Act .\n#### 2. Disclosure requirements for Federal funds\n##### (a) In general\nSubchapter III of chapter 13 of title 31, United States Code, is amended by adding at the end the following:\n1356. Disclosure requirements for Federal funds (a) Definition In this section, the term agency means\u2014 (1) an Executive agency, as defined in section 105 of title 5; and (2) an independent regulatory agency, as defined in section 3502 of title 44. (b) Disclosure requirements An agency and an individual or entity (including a State or local government and a recipient of a Federal research grant) carrying out a program, project, or activity that is, in whole or in part, carried out using Federal funds shall clearly state in any statement, press release, request for proposals, bid solicitation, or other document describing the program, project, or activity, other than a communication containing not more than 280 characters\u2014 (1) the percentage of the total costs of the program, project, or activity which will be financed with Federal funds; (2) the dollar amount of the Federal funds made available for the program, project, or activity; and (3) the percentage of the total costs of, and dollar amount for, the program, project, or activity that will be financed by nongovernmental sources. (c) Certification An individual or entity carrying out a program, project, or activity that is, in whole or in part, carried out using Federal funds shall, as part of the performance progress reporting regarding the program, project, or activity, include a certification indicating whether the individual or entity complied with the disclosure requirements. (d) Compliance review The Director of the Office of Management and Budget shall annually\u2014 (1) review a random sampling of public communications issued by agencies and recipients of Federal funds for compliance with the disclosure requirements under subsection (b); and (2) make publicly available the findings of the review under paragraph (1). (e) Public reporting Not later than 1 year after the date of enactment of this section, the Director of the Office of Management and Budget shall make available to the public a mechanism to anonymously report communications that do not comply with the disclosure requirements under subsection (b), which shall require that such a report include\u2014 (1) the noncompliant communication or, if publicly available, the location of the noncompliant communication; and (2) identifying information regarding the program, project, or activity that is, in whole or in part, carried out using Federal funds. .\n##### (b) Technical and conforming amendment\nThe table of sections for subchapter III of chapter 13 of title 31, United States Code, is amended by adding at the end the following:\n1356. Disclosure requirements for Federal funds. .",
      "versionDate": "2025-02-14",
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
        "actionDate": "2026-03-18",
        "text": "Committee on Small Business and Entrepreneurship. Hearings held."
      },
      "number": "4130",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "COST Act",
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
        "item": {
          "name": "Government information and archives",
          "updateDate": "2025-07-08T13:00:41Z"
        }
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-08T12:47:18Z"
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
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1387ih.xml"
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
      "title": "COST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cost Openness and Spending Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the disclosure of information relating to the cost of programs, projects, or activities carried out using Federal funds.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:20:42Z"
    }
  ]
}
```
