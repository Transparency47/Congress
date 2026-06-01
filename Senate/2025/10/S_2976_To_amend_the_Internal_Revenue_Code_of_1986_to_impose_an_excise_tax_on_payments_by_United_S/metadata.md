# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2976?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2976
- Title: HIRE Act
- Congress: 119
- Bill type: S
- Bill number: 2976
- Origin chamber: Senate
- Introduced date: 2025-10-06
- Update date: 2026-03-09T19:18:57Z
- Update date including text: 2026-03-09T19:18:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-06: Introduced in Senate
- 2025-10-06 - IntroReferral: Introduced in Senate
- 2025-10-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-10-06: Introduced in Senate

## Actions

- 2025-10-06 - IntroReferral: Introduced in Senate
- 2025-10-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-06",
    "latestAction": {
      "actionDate": "2025-10-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2976",
    "number": "2976",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "HIRE Act",
    "type": "S",
    "updateDate": "2026-03-09T19:18:57Z",
    "updateDateIncludingText": "2026-03-09T19:18:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-06",
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
      "actionDate": "2025-10-06",
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
          "date": "2025-10-06T23:17:02Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2976is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2976\nIN THE SENATE OF THE UNITED STATES\nOctober 6, 2025 Mr. Moreno introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to impose an excise tax on payments by United States taxpayers to foreign persons for services provided to United States consumers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Halting International Relocation of Employment Act or the HIRE Act .\n#### 2. Outsourcing excise tax\n##### (a) In general\nSubtitle D of the Internal Revenue Code of 1986 is amended by adding at the end the following new chapter:\n50B Outsourcing Sec. 5000E. Outsourcing payments. 5000E. Outsourcing payments (a) Imposition of tax There is hereby imposed a tax on any United States person making an outsourcing payment a tax equal to 25 percent of the amount of such payment. (b) Outsourcing payment For purposes of this section\u2014 (1) In general The term outsourcing payment means any premium, fee, royalty, service charge, or other payment made\u2014 (A) in the course of a trade or business, (B) to a foreign person, and (C) with respect to labor or services the benefit of which is directed, directly or indirectly, to consumers located in the United States. (2) Mixed payments In the case of any payment to a foreign person with respect to which labor or services are directed to consumers both within and without the United States, the amount treated as an outsourcing payment shall not exceed the amount equal to the product of such payment and a fraction\u2014 (A) the numerator of which is the amount of labor or services with respect to such payment directed to consumers within the United States, to (B) the labor or services with respect to such payment directed to all consumers. (c) Foreign person For purposes of this section, the term foreign person means any person who is not a United States person, except that such term shall not include any corporation or partnership which is organized under the laws of a possession of the United States. (d) Regulations and other guidance The Secretary shall prescribe such regulations and other guidance as may be necessary or appropriate to carry out this section, including regulations or guidance to prevent the avoidance or abuse of the purposes of this section, including through the use of related parties, controlled foreign corporations, and other intermediaries, or through the use of transfer pricing arrangements. .\n##### (b) Tax not deductible\nSection 275(a)(6) of the Internal Revenue Code of 1986 is amended by inserting 50B, after 50A .\n##### (c) Reporting\nThe Secretary of the Treasury, or the Secretary's delegate, may\u2014\n**(1)**\nrequire United States persons making payments to foreign persons (as defined in section 5000E of the Internal Revenue Code of 1986, as added by subsection (a)) to file a return of tax under section 5000E of such Code or to file an information return concerning such payments, which may include\u2014\n**(A)**\ninformation on whether such payments are outsourcing payments (as defined in section 5000E of such Code), and\n**(B)**\nsuch other information concerning such payment as the Secretary may reasonably require to enforce the amendments made by this section, and\n**(2)**\nrequire the officers of any corporation to certify on such return, under penalty of perjury, the character of such payments.\nchapter 68\n##### (d) Increased penalty for failure To pay tax\nSection 6651(a) of the Internal Revenue Code is amended by adding at the end the following new sentence: In the case of the failure to pay any tax imposed under chapter 50B, paragraphs (2) and (3) shall be applied by substituting 50 percent for 05. percent each place it appears and without regard to the phrase not exceeding 25 percent in the aggregate each place it appears. .\n##### (e) No inference\nNothing in this section or the amendments made by this section shall be construed to limit the application of the economic substance doctrine with respect to any payment described in section 5000E(b) of the Internal Revenue Code of 1986, as added by subsection (a).\n##### (f) Clerical amendment\nThe table of chapters for subpart D of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nChapter 50B\u2014Outsourcing .\n##### (g) Effective date\nThe amendments made by this section shall apply to payments made after December 31, 2025.\n#### 3. Domestic workforce fund\n##### (a) In general\nSubchapter A of chapter 98 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n9512. Domestic workforce fund (a) Establishment There is established in the Treasury of the United States a trust fund to be known as the Domestic Workforce Fund (hereafter in this section referred to as the Fund ), consisting of such amounts as may be appropriated, credited, or paid into the Fund as provided in this section or section 9602(b). (b) Transfer to fund There are hereby appropriated to the Fund amounts equivalent to the amounts received in the Treasury under\u2014 (1) the tax imposed under section 5000E, (2) so much of the additions to tax under section 6051(a) as relates to the failure to pay taxes imposed under section 5000E, and (3) so much of the penalties imposed under part II of suchchapter B of chapter 68 as relates to returns described in section 2(b) of the Halting International Relocation of Employment Act . (c) Expenditures from fund Amounts in the Fund shall be available, without further appropriation, solely for the following purposes: (1) Workforce development and retraining programs administered by the Department of Labor. (2) Apprenticeship programs and partnerships with industry to expand domestic employment in sectors impacted by outsourcing. (3) Grants to States for workforce development initiatives targeted at communities with high levels of job displacement. .\n##### (b) Clerical amendment\nThe table of sections for subchapter A of chapter 98 of such Code is amended by adding at the end the following new item:\nSec. 9512. Domestic workforce fund. .\n#### 4. Denial of income tax deduction on outsourcing payments\n##### (a) In general\nPart IX of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n280I. Outsourcing payments No deduction shall be allowed under this chapter for any outsourcing payment (as defined in section 5000E(b)). .\n##### (b) Clerical amendment\nThe table of section for part IX of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 280I. Outsourcing payments. .\n##### (c) Effective date\nThe amendments made by this section shall apply to payments made after December 31, 2025, in taxable years ending after such date.",
      "versionDate": "2025-10-06",
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
        "actionDate": "2026-02-12",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7559",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to deny deduction for outsourcing payments.",
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
        "updateDate": "2025-11-21T16:32:51Z"
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
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2976is.xml"
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
      "title": "HIRE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-18T03:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HIRE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T03:23:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Halting International Relocation of Employment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T03:23:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to impose an excise tax on payments by United States taxpayers to foreign persons for services provided to United States consumers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-18T03:18:11Z"
    }
  ]
}
```
