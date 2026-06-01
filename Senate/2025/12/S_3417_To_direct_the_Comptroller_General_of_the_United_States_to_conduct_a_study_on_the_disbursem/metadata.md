# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3417?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3417
- Title: Main Street Lending Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3417
- Origin chamber: Senate
- Introduced date: 2025-12-10
- Update date: 2026-01-14T04:58:01Z
- Update date including text: 2026-01-14T04:58:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in Senate
- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2025-12-10: Introduced in Senate

## Actions

- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3417",
    "number": "3417",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "J000312",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Justice, James C. [R-WV]",
        "lastName": "Justice",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Main Street Lending Improvement Act of 2025",
    "type": "S",
    "updateDate": "2026-01-14T04:58:01Z",
    "updateDateIncludingText": "2026-01-14T04:58:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T18:20:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3417is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3417\nIN THE SENATE OF THE UNITED STATES\nDecember 10, 2025 Mr. Justice introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo direct the Comptroller General of the United States to conduct a study on the disbursement process for certain small business loans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Main Street Lending Improvement Act of 2025 .\n#### 2. Disbursement process for certain small business loans\n##### (a) Definitions\nIn this section:\n**(1) Appalachian region**\nThe term Appalachian region has the meaning given such term by section 14102(a) of title 40, United States Code.\n**(2) Covered region**\nThe term covered region means a region of the Administration that includes any part of the Appalachian region.\n**(3) Region of the Administration**\nThe term region of the Administration has the meaning given such term in section 3 of the Small Business Act ( 15 U.S.C. 632 ).\n**(4) Small business concern**\nThe term small business concern has the meaning given such term under section 3 of the Small Business Act ( 15 U.S.C. 632(a) ).\n**(5) Small business loan**\nThe term small business loan means a loan made under title V of the Small Business Investment Act of 1958 ( 15 U.S.C. 695 et seq. ), section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ), or section 7(m) of the Small Business Act ( 15 U.S.C. 636(m) ), except that such term excludes any loan made under a program established in response to the COVID\u201319 pandemic.\n##### (b) Study\nThe Comptroller General of the United States shall conduct a study on the disbursement process for small business loans.\n##### (c) Contents\n**(1) In general**\nIn conducting the study under subsection (b), the Comptroller General shall determine for each year during the period beginning on January 1, 2021, and ending on December 31, 2024, for each covered region, the measures described in paragraph (2).\n**(2) Measures described**\nThe measures described in this paragraph with respect to a covered region are, for each of the portion of such covered region that is part of the Appalachian region and the portion of such covered region that is not part of the Appalachian region\u2014\n**(A)**\nthe average length of time\u2014\n**(i)**\nbetween the submission of an application for a small business loan by a small business concern for which the principal place of business is located in such portion and when funds are disbursed with respect to such application; and\n**(ii)**\nto complete each step of the application and disbursement process for small business loans for small business concerns for which the principal place of business is located in such portion;\n**(B)**\nthe number that is equal to the product of\u2014\n**(i)**\nthe number of small business loans disbursed to small business concerns for which the principal place of business is located in such portion divided by the total number of small business concerns for which the principal place of business is located in such portion; and\n**(ii)**\n1000;\n**(C)**\nthe number that is equal to the product of\u2014\n**(i)**\nthe number of small business loans approved for small business concerns for which the principal place of business is located in such portion divided by the total number of small business concerns for which the principal place of business is located in such portion; and\n**(ii)**\n1000;\n**(D)**\nthe average and median dollar amount of small business loans disbursed to small business concerns for which the principal place of business is located in such portion; and\n**(E)**\nthe number that is equal to the product of\u2014\n**(i)**\nthe aggregate dollar amount of all small business loans disbursed to small business concerns for which the principal place of business is located in such portion divided by the total number of small business concerns for which the principal place of business is located in such portion; and\n**(ii)**\n1000.\n##### (d) Briefing and report\n**(1) Interim briefing**\nNot later than 1 year after the date of enactment of this Act, the Comptroller General shall provide to Congress a briefing on the progress of the study required by subsection (b).\n**(2) Report**\n**(A) In general**\nNot later than 2 years after the date of enactment of this Act, the Comptroller General shall submit to Congress a report containing the results of the study required by subsection (b).\n**(B) Recommendations**\nThe report required by subparagraph (A) shall include recommendations of the Comptroller General for changes to the small business loan disbursement process to\u2014\n**(i)**\nincrease accessibility of small business loans;\n**(ii)**\ndecrease the average length of time from when an application for a small business loan is submitted to when funds are disbursed with respect to such application;\n**(iii)**\nincrease the availability of information to an applicant for a small business loan regarding the status of the application of such applicant, including if any additional information is needed from the applicant to continue processing the application of such applicant and an estimate of the length of time until the funds with respect to such application will be disbursed; and\n**(iv)**\nidentify mechanisms and processes internal to the agencies involved in making small business loans that can be changed to reduce inefficiencies of the Government with respect to the processing of applications for small business loans.",
      "versionDate": "2025-12-10",
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
        "actionDate": "2025-12-10",
        "text": "Referred to the House Committee on Small Business."
      },
      "number": "6600",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Main Street Lending Improvement Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2026-01-08T17:14:59Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3417is.xml"
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
      "title": "Main Street Lending Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:39:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Main Street Lending Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:39:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Comptroller General of the United States to conduct a study on the disbursement process for certain small business loans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:33:40Z"
    }
  ]
}
```
