# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3114?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3114
- Title: Union Members Right to Know Act
- Congress: 119
- Bill type: S
- Bill number: 3114
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2025-12-03T12:03:24Z
- Update date including text: 2025-12-03T12:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3114",
    "number": "3114",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Union Members Right to Know Act",
    "type": "S",
    "updateDate": "2025-12-03T12:03:24Z",
    "updateDateIncludingText": "2025-12-03T12:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
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
      "actionDate": "2025-11-06",
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
          "date": "2025-11-06T16:10:11Z",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "TN"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "IA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "AL"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3114is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3114\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. Cassidy (for himself, Mrs. Blackburn , Ms. Ernst , and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Labor-Management Reporting and Disclosure Act of 1959 to require labor organizations to make certain disclosures to its members, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Union Members Right to Know Act .\n#### 2. Amendments to the Labor-Management Reporting and Disclosure Act of 1959\n##### (a) Required disclosures\nSection 105 of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 415 ) is amended\u2014\n**(1)**\nby striking Every and inserting the following:\n(a) In general Every ; and\n**(2)**\nby adding at the end the following:\n(b) Required disclosures (1) In general Every labor organization shall provide to each member of the labor organization, in accordance with paragraph (2), the following: (A) A copy of this Act and a summary of each title of this Act. (B) A summary of the rights of an individual to seek, pursuant to title VII of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e et seq. ), a reasonable accommodation, based on the religious beliefs or practices of the individual, not to pay dues or fees to the labor organization. (C) A summary of the rights of employees under the holding of the Supreme Court of the United States in Communications Workers v. Beck, 487 U.S. 735 (1988). (2) Disclosure requirements Every labor organization shall provide the information under paragraph (1) by\u2014 (A) mail or electronic mail\u2014 (i) (I) to each employee who joins the labor organization on or after the date that is 90 days after the date of enactment of the Union Members Right to Know Act , not later than 30 days after the employee joins the labor organization; and (II) to each member of the labor organization who was a member on the day before the date that is 90 days after the date of enactment of the Union Members Right to Know Act , not later than 1 year after such date of enactment; and (ii) on an annual basis; and (B) if the labor organization has a website, maintaining on the home-page of the website of the labor organization a hyperlink, titled Union Member Rights and Officer Responsibilities Under the LMRDA , to the information described under paragraph (1). (3) Compliance (A) Initial compliance Not later than 180 days after such date of enactment, every labor organization that is required to comply with paragraph (2)(B) shall submit to the Secretary a form signed by its president and treasurer, or corresponding principal officers, certifying that the labor organization has complied with the requirements of such paragraph. (B) Ongoing compliance Not later than 18 months after such date of enactment, and on an annual basis thereafter, each labor organization shall submit to the Secretary a form signed by its president and treasurer, or corresponding principal officers, certifying that the labor organization has complied with the requirements of paragraph (2). .\n##### (b) Right not To subsidize labor organization nonrepresentational activities\nTitle I of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 411 et seq. ) is amended by adding at the end the following:\n106. Right not to subsidize labor organization nonrepresentational activities No employee\u2019s labor organization dues, fees, assessments, or other contributions shall be used or contributed to any person, organization, or entity for any purpose not directly related to the labor organization\u2019s collective bargaining or contract administration functions on behalf of the represented unit employee unless the employee member, or nonmember required to make such payments as a condition of employment, authorizes such expenditure in writing, after a notice period of not less than 35 days. An initial authorization provided by an employee under the preceding sentence shall expire not later than 1 year after the date on which such authorization is signed by the employee. There shall be no automatic renewal of an authorization under this section. .\n#### 3. Regulations\nNot later than 180 days after the date of enactment of this Act, the Secretary of Labor shall issue such regulations as are necessary to implement the amendments made by section 2 of this Act.",
      "versionDate": "2025-11-06",
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
        "name": "Labor and Employment",
        "updateDate": "2025-11-19T15:34:35Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3114is.xml"
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
      "title": "Union Members Right to Know Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Union Members Right to Know Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Labor-Management Reporting and Disclosure Act of 1959 to require labor organizations to make certain disclosures to its members, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:33:16Z"
    }
  ]
}
```
