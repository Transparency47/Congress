# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1247?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1247
- Title: Public Safety Free Speech Act
- Congress: 119
- Bill type: S
- Bill number: 1247
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2026-04-27T14:53:44Z
- Update date including text: 2026-04-27T14:53:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1247",
    "number": "1247",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Public Safety Free Speech Act",
    "type": "S",
    "updateDate": "2026-04-27T14:53:44Z",
    "updateDateIncludingText": "2026-04-27T14:53:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-02",
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
      "actionDate": "2025-04-02",
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
            "date": "2025-04-02T16:10:27Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-02T16:10:27Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "IN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-03-10",
      "state": "AK"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1247is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1247\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mr. Schmitt introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo ensure the ability of public safety officers to retain their right to free speech on matters related to public safety, working conditions, and other matters.\n#### 1. Short title\nThis Act may be cited as the Public Safety Free Speech Act .\n#### 2. Definitions\nIn this Act:\n**(1) Covered employee**\nThe term covered employee means\u2014\n**(A)**\na qualified law enforcement officer (as defined in section 926B(c) of title 18, United States Code);\n**(B)**\nan individual employed by an employer for the purposes of providing fire-fighting services or emergency medical services; or\n**(C)**\na Federal firefighter described in section 8331(21) or 8401(14) of title 5, United States Code.\n**(2) Employer**\nThe term employer means\u2014\n**(A)**\na law enforcement agency, fire department, fire district, or emergency medical services agency which employs a covered employee on either a full-time or part-time basis; or\n**(B)**\na county, township, village, city, municipality, special district, fire authority, county improvement district, authority, public entity with the authority to spend or receive public funds, or other political subdivisions of a State and includes any entity jointly created by 2 or more public employers.\n**(3) Personally identifiable information**\nThe term personally identifiable information means information\u2014\n**(A)**\nthat directly identifies an individual, including name, address, social security number or other identifying number or code, telephone number, email address; or\n**(B)**\nby which an organization is able to identify specific individuals in conjunction with other data elements.\n#### 3. Cause of action for violating the right to free speech\n##### (a) In general\nNotwithstanding any other provision of law, a covered employee may bring an action against an employer if the employer engages in termination or any adverse employment action against the employee for making oral or written statements expressing the employee\u2019s personal opinion on matters pertaining to\u2014\n**(1)**\ndelivery of public safety services;\n**(2)**\nemployee compensation or benefits;\n**(3)**\nworking conditions or scheduling, including the provision of personal protective equipment, work tools and equipment, or work vehicles;\n**(4)**\nemployer\u2019s policies or procedures;\n**(5)**\nother expectations or requirements that the employer places on a covered employee as a term or condition of their employment; or\n**(6)**\npolitical and religious opinions.\n##### (b) Relief\nA plaintiff that prevails in an action under subsection (a) may receive actual damages, compensatory damages, punitive damages, injunctive relief, any combination of those, attorneys\u2019 fees and costs, and any other appropriate relief.\n##### (c) Limitations\nSubsection (a) shall not apply to written or oral comments that\u2014\n**(1)**\nare made while the covered employee is on duty;\n**(2)**\nexpress any encouragement of, or intent, to commit violence or other illegal actions;\n**(3)**\nadvocate for discrimination or support favoritism when discharging their professional duties;\n**(4)**\nintentionally disclose confidential or personally identifiable information pertaining to specific individuals with whom the covered employee has interacted with in the course of performing their work or other job-related duties; or\n**(5)**\nsuggest, advocate for, support, or otherwise communicate that essential services should be withheld, delayed, or diminished as a form of job action or protest.\n42 U.S.C. 1983",
      "versionDate": "2025-04-02",
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
        "actionDate": "2025-02-18",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1443",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Public Safety Free Speech Act",
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
            "name": "Employee performance",
            "updateDate": "2026-04-27T14:53:38Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2026-04-27T14:53:44Z"
          },
          {
            "name": "First Amendment rights",
            "updateDate": "2026-04-27T14:53:26Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2026-04-27T14:53:31Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2026-04-27T14:53:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-04-17T15:09:20Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1247is.xml"
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
      "title": "Public Safety Free Speech Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Public Safety Free Speech Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure the ability of public safety officers to retain their right to free speech on matters related to public safety, working conditions, and other matters.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:48:36Z"
    }
  ]
}
```
