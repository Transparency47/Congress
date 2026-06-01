# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2219?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2219
- Title: Salary History Question Prohibition Act
- Congress: 119
- Bill type: HR
- Bill number: 2219
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-09-29T20:53:00Z
- Update date including text: 2025-09-29T20:53:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-03-18 - IntroReferral: Sponsor introductory remarks on measure. (CR E225)
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-03-18 - IntroReferral: Sponsor introductory remarks on measure. (CR E225)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2219",
    "number": "2219",
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
    "title": "Salary History Question Prohibition Act",
    "type": "HR",
    "updateDate": "2025-09-29T20:53:00Z",
    "updateDateIncludingText": "2025-09-29T20:53:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E225)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:03:35Z",
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
      "sponsorshipDate": "2025-05-08",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2219ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2219\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Fair Labor Standards Act of 1938 to prohibit certain practices by employers relating to restrictions on discussion of employees' and prospective employees' salary and benefit history, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Salary History Question Prohibition Act .\n#### 2. Prohibitions relating to prospective employees\u2019 salary and benefit history\n##### (a) In general\nThe Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) is amended by inserting after section 7 the following new section:\n8. Requirements and prohibitions relating to wage, salary, and benefit history (a) In general It shall be an unlawful practice for an employer to\u2014 (1) rely on the wage history of a prospective employee in considering the prospective employee for employment, including requiring that a prospective employee\u2019s prior wages satisfy minimum or maximum criteria as a condition of being considered for employment; (2) rely on the wage history of a prospective employee in determining the wages for such prospective employee, except that an employer may rely on wage history if it is voluntarily provided by a prospective employee, after the employer makes an offer of employment with an offer of compensation to the prospective employee, to support a wage higher than the wage offered by the employer; (3) seek from a prospective employee or any current or former employer the wage history of the prospective employee, except that an employer may seek to confirm prior wage information only after an offer of employment with compensation has been made to the prospective employee and the prospective employee responds to the offer by providing prior wage information to support a wage higher than that offered by the employer; or (4) discharge or in any other manner retaliate against any employee or prospective employee because the employee or prospective employee\u2014 (A) opposed any act or practice made unlawful by this section; or (B) took an action for which discrimination is forbidden under section 15(a)(3). (b) Definition In this section, the term wage history means the wages paid to the prospective employee by the prospective employee\u2019s current employer or previous employer. .\n##### (b) Penalties\nSection 16 of such Act ( 29 U.S.C. 216 ) is amended by adding at the end the following new subsection:\n(f) (1) Any person who violates the provisions of section 8 shall\u2014 (A) be subject to a civil penalty of $5,000 for a first offense, increased by an additional $1,000 for each subsequent offense, not to exceed $10,000; and (B) be liable to each employee or prospective employee who was the subject of the violation for special damages not to exceed $10,000 plus attorneys\u2019 fees, and shall be subject to such injunctive relief as may be appropriate. (2) An action to recover the liability described in paragraph (1)(B) may be maintained against any employer (including a public agency) in any Federal or State court of competent jurisdiction by any one or more employees or prospective employees for and on behalf of\u2014 (A) the employees or prospective employees; and (B) other employees or prospective employees similarly situated. .",
      "versionDate": "2025-03-18",
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
        "actionDate": "2025-03-25",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1115",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Paycheck Fairness Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-25",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "17",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Paycheck Fairness Act",
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
        "name": "Labor and Employment",
        "updateDate": "2025-04-04T12:52:26Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2219ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Labor Standards Act of 1938 to prohibit certain practices by employers relating to restrictions on discussion of employees' and prospective employees' salary and benefit history, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:33Z"
    },
    {
      "title": "Salary History Question Prohibition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Salary History Question Prohibition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:21Z"
    }
  ]
}
```
