# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1459?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1459
- Title: Historic Tax Credit Growth and Opportunity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1459
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-03-04T12:40:47Z
- Update date including text: 2026-03-04T12:40:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1459",
    "number": "1459",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
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
    "title": "Historic Tax Credit Growth and Opportunity Act of 2025",
    "type": "S",
    "updateDate": "2026-03-04T12:40:47Z",
    "updateDateIncludingText": "2026-03-04T12:40:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
            "date": "2025-04-10T18:50:30Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-10T18:50:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "VA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "ME"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "WA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "MN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "MS"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "MN"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "IN"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "IN"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-03",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1459is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1459\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Cassidy (for himself, Mr. Warner , Ms. Collins , and Ms. Cantwell ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to improve the historic rehabilitation tax credit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Historic Tax Credit Growth and Opportunity Act of 2025 .\n#### 2. Full credit allowed in the year building placed in service\n##### (a) In general\nSection 47(a) of the Internal Revenue Code of 1986 is amended to read as follows:\n(a) General rule For purposes of section 46, the rehabilitation credit for any taxable year is 20 percent of the qualified rehabilitation expenditures. .\n##### (b) Effective date\nThe amendment made by this section shall apply to property placed in service after December 31, 2023.\n#### 3. Increase in the rehabilitation credit for certain small projects\n##### (a) In general\nSection 47 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(e) Special rule regarding certain small projects (1) In general In the case of any qualifying small project with respect to which there is an election in effect under this subsection\u2014 (A) the total qualified rehabilitation expenditures taken into account for purposes of this section with respect to the rehabilitation shall not exceed $3,750,000, (B) subsection (a) shall be applied by substituting 30 percent for 20 percent , and (C) subject to paragraph (4) and such regulations or other guidance as the Secretary may provide, the taxpayer may transfer all or a portion of the credit determined under this section with respect to such qualifying small project. (2) Qualifying small project For purposes of this subsection, the term qualifying small project means any qualified rehabilitated building or portion thereof if\u2014 (A) such building is placed in service after the date of the enactment of this subsection, and (B) no credit was allowed under this section (other than a credits allowed by reason of subsection (d)) for either of the two immediately preceding taxable years with respect to such building. (3) Special rule for rural projects (A) In general In the case of any qualifying small project in a rural area, paragraph (1)(A) shall be applied by substituting $5,000,000 for $3,750,000 . (B) Rural area For purposes of this subparagraph, the term rural area means any area other than\u2014 (i) a city or town that has a population of greater than 50,000 inhabitants, or (ii) the urbanized area contiguous and adjacent to a city or town described in clause (i), as defined by the Bureau of the Census based on the latest decennial census of the United States. (4) Transfer of credit for qualifying small projects (A) Certification (i) In general A transfer under paragraph (1)(C)) shall be accompanied by a certificate which includes\u2014 (I) the certification for the certified historic structure referred to in subsection (c)(3), (II) the taxpayer\u2019s name, address, tax identification number, date of project completion, and the amount of credit being transferred, (III) the transferee\u2019s name, address, tax identification number, and the amount of credit being transferred, and (IV) such other information as may be required by the Secretary. (ii) Transferability of certificate A certificate issued under this subsection to a taxpayer shall be transferable to any other taxpayer. (B) Tax treatment relating to certificate (i) Disallowance of deduction No deduction shall be allowed for the amount of consideration paid or incurred by the transferee. (ii) Allowance of credit The amount of credit transferred under paragraph (1)(C)\u2014 (I) shall not be allowed to the transferor for any taxable year, and (II) shall be allowable to the transferee as a credit determined under this section for the taxable year of the transferee in which such credit is transferred. (iii) Exclusion Gross income shall not include any amount received in connection with the transfer of the certificate. (C) Recapture and other special rules The taxpayer who claims a credit determined under this section by reason of a transfer of an amount of credit under paragraph (1)(A) with respect to an applicable rural project shall be treated as the taxpayer with respect to such project for purposes of section 50. (D) Information reporting The transferor and the transferee shall each make such reports regarding the transfer of an amount of credit under paragraph (1)(C) and containing such information as the Secretary may require. The reports required by this subparagraph shall be filed at such time and in such manner as may be required by the Secretary. (E) Regulations The Secretary shall prescribe regulations or other guidance to carry out paragraph (1)(C) and this paragraph in a manner which is consistent with applicable requirements with respect to transfer of credits under section 6418. (5) Election An election under this subsection shall be made at such time and in such manner as the Secretary may by regulations prescribe. .\n##### (b) Effective date\nThe amendment made by this section shall apply to property placed in service after the date of the enactment of this Act.\n#### 4. Increasing the type of buildings eligible for rehabilitation\n##### (a) In general\nSection 47(c)(1)(B)(i)(I) of the Internal Revenue Code of 1986 is amended by inserting 50 percent of before the adjusted basis .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply to property placed in service after the date of the enactment of this Act..\n#### 5. Elimination of rehabilitation credit basis adjustment\n##### (a) In general\nSection 50(c) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(6) Exception for rehabilitation credit In the case of the rehabilitation credit, paragraph (1) shall not apply. .\n##### (b) Treatment in case of credit allowed to lessee\nSection 50(d) of such Code is amended by adding at the end the following: In the case of the rehabilitation credit, paragraph (5)(B) of the section 48(d) referred to in paragraph (5) of this subsection shall not apply. .\n##### (c) Effective date\nThe amendments made by this section shall apply to property placed in service after the date of the enactment of this Act.\n#### 6. Modifications regarding certain tax-exempt use property\n##### (a) In general\nSection 47(c)(2)(B)(v) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subclause:\n(III) Disqualified lease rules to apply only in case of government entity For purposes of subclause (I), except in the case of a tax-exempt entity described in section 168(h)(2)(A)(i), the determination of whether property is tax-exempt use property shall be made under section 168(h) without regard to whether the property is leased in a disqualified lease (as defined in section 168(h)(1)(B)(ii)). .\n##### (b) Effective date\nThe amendments made by this section shall apply to property placed in service after the date of the enactment of this Act.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6900",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Affordability Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-17",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2941",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Historic Tax Credit Growth and Opportunity Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-05-12T20:02:56Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1459is.xml"
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
      "title": "Historic Tax Credit Growth and Opportunity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-04T12:40:47Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Historic Tax Credit Growth and Opportunity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T02:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to improve the historic rehabilitation tax credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T02:18:15Z"
    }
  ]
}
```
