# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2007?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2007
- Title: Salary Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 2007
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-03-06T20:42:00Z
- Update date including text: 2026-03-06T20:42:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-03-10 - IntroReferral: Sponsor introductory remarks on measure. (CR E198)
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-03-10 - IntroReferral: Sponsor introductory remarks on measure. (CR E198)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2007",
    "number": "2007",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Salary Transparency Act",
    "type": "HR",
    "updateDate": "2026-03-06T20:42:00Z",
    "updateDateIncludingText": "2026-03-06T20:42:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E198)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "MI"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2007ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2007\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Fair Labor Standards Act to require an employer providing an employment opportunity to disclose the wage range for such employment opportunity to employees and applicants for employment, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Salary Transparency Act .\n#### 2. Prohibitions relating to wage disclosures\n##### (a) In general\nThe Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) is amended by inserting after section 7 the following new section:\n8. Requirements and prohibitions relating to wage disclosures (a) In general It shall be an unlawful practice for an employer to\u2014 (1) fail or refuse to disclose, in any public or internal posting for an employment opportunity, the wage or wage range for such employment opportunity; (2) in any case in which a public or internal posting for an employment opportunity has not been made available to an applicant for such employment opportunity, fail or refuse to disclose to such applicant the wage or wage range for such employment opportunity prior to discussing compensation with the applicant and at any time upon the applicant\u2019s request; (3) fail or refuse to disclose to an employee the wage or wage range for the employee\u2019s position upon hire and at least annually thereafter and at any time upon the employee\u2019s request; or (4) refuse to interview, hire, promote, or employ an employee or applicant for employment, or in any other manner retaliate against an employee or applicant for employment, for exercising any rights under this section. (b) Definition In this section, the term wage range , with respect to an employment opportunity, means the range of wages, or salaries and other forms of compensation, that the employer providing such employment opportunity anticipates in good faith relying on in setting the pay for such employment opportunity. Such term may include reference to any applicable pay scale, previously determined wage range for the position, the actual wage range for those currently holding equivalent positions, or the budgeted amount for the position, as applicable. For the purposes of subsection (a)(3), such term may include reference to any applicable pay scale, previously determined wage range for the position, or the wage range for incumbents in equivalent positions, as applicable. .\n##### (b) Penalties\nSection 16 of such Act ( 29 U.S.C. 216 ) is amended by adding at the end the following new subsection:\n(f) (1) Any person who violates the provisions of section 8 shall\u2014 (A) be subject to a civil penalty of $5,000 for a first violation, increased by an additional $1,000 for each subsequent violation, not to exceed $10,000; and (B) be liable to each employee or applicant for employment who was the subject of the violation for statutory damages between $1,000 and $10,000, or actual damages, whichever is greater, plus reasonable attorneys\u2019 fees, and shall be subject to such injunctive relief as may be appropriate. (2) An action to recover the liability described in paragraph (1)(B) may be maintained against any employer (including a public agency) in any Federal or State court of competent jurisdiction by any one or more employees or applicants for employment for and on behalf of\u2014 (A) the employees or applicants for employment; and (B) other employees or applicants for employment similarly situated. .",
      "versionDate": "2025-03-10",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-03-06T20:42:00Z"
          },
          {
            "name": "Labor standards",
            "updateDate": "2026-03-06T20:41:56Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-03-06T20:41:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-26T17:30:51Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2007ih.xml"
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
      "title": "Salary Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Salary Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Labor Standards Act to require an employer providing an employment opportunity to disclose the wage range for such employment opportunity to employees and applicants for employment, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:48Z"
    }
  ]
}
```
