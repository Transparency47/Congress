# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1753?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1753
- Title: Community News and Small Business Support Act
- Congress: 119
- Bill type: HR
- Bill number: 1753
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-05-13T20:00:12Z
- Update date including text: 2026-05-13T20:00:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1753",
    "number": "1753",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Community News and Small Business Support Act",
    "type": "HR",
    "updateDate": "2026-05-13T20:00:12Z",
    "updateDateIncludingText": "2026-05-13T20:00:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:13:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "WA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "GA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CO"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "RI"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "VA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NH"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1753ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1753\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Ms. Tenney (for herself and Ms. DelBene ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide tax incentives that support local media.\n#### 1. Short title\nThis Act may be cited as the Community News and Small Business Support Act .\n#### 2. Credit for advertising in local media\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Advertising in local media (a) In general For purposes of section 38, in the case of any eligible small business, the local media advertising credit determined under this section for any taxable year is an amount equal to the applicable percentage of the qualified local media advertising expenses paid or incurred by the taxpayer during such taxable year. (b) Limitation The credit allowed under subsection (a) to any taxpayer for any taxable year shall not exceed\u2014 (1) in the case of the first taxable year to which this section applies, $5,000, and (2) in the case of any subsequent taxable year, $2,500. (c) Applicable percentage For purposes of this section, the term applicable percentage means\u2014 (1) in the case of the first taxable year to which this section applies, 80 percent, and (2) in the case of any subsequent taxable year, 50 percent. (d) Eligible small business For purposes of this section, the term eligible small business means any person for any taxable year if the average number of full-time employees (as determined for purposes of determining whether an employer is an applicable large employer for purposes of section 4980H(c)(2) of the Internal Revenue Code of 1986) employed by such person during such taxable year was less than 50. (e) Qualified local media advertising expenses For purposes of this section, the term qualified local media advertising expenses means amounts paid or incurred in the ordinary course of a trade or business for\u2014 (1) advertising in a local newspaper, or (2) advertising on any broadcast radio or television station licensed by the Federal Communications Commission to serve a local community. For purposes of this subsection, the term advertising includes sponsorships. (f) Local newspaper For purposes of this section\u2014 (1) In general The term local newspaper means any print or digital publication if\u2014 (A) the primary content of such publication is original content derived from primary sources and relating to news and current events, (B) such publication primarily serves the needs of a regional or local community, (C) the publisher of such publication\u2014 (i) employs at least one full-time local news journalist who resides in such regional or local community, (ii) employs not greater than 750 employees, and (iii) is not\u2014 (I) an organization described in paragraph (4), (5), or (6) of section 501(c), (II) a political organization (as defined in section 527(e)), (III) any organization controlled by one or more organizations described in subclauses (I) or (II), or (IV) any organization that received more than $100,000 (in the aggregate) from organizations described in subclauses (I), (II), or (III) during the taxable year or any preceding taxable year. (2) Local news journalist For purposes of paragraph (1)(C)(i), the term local news journalist means any individual who regularly gathers, prepares, produces, collects, edits, photographs, records, directs the recording of, writes, presents, or reports news or information that concerns local events or other matters of local public interest. (3) Aggregation rule (A) In general For purposes of clauses (ii) and (iii) of paragraph (1)(C), all persons treated as a single employer under subsection (a) or (b) of section 52, or subsection (m) or (o) of section 414, shall be treated as one person. (B) Exception Subparagraph (A) shall not apply unless such persons are involved in the production of the same print or digital publication. (4) Continuous qualification The requirements of paragraph (1)(C) shall not be treated as met unless such requirements are met at all times during the period beginning on the date which is 1 year before the date of the enactment of this section and ending on the date that the subscription described in subsection (a) is paid or incurred. (g) Special rules (1) Denial of double benefit No deduction shall be allowed for any qualified local media advertising expenses otherwise allowable as a deduction for the taxable year which is equal to the amount of the credit determined for such taxable year under subsection (a). (2) Aggregation rule All persons treated as a single employer under subsection (a) or (b) of section 52 of the Internal Revenue Code of 1986, or subsection (m) or (o) of section 414 of such Code, shall be treated as one person for purposes of applying subsection (b). (h) Termination No credit shall be allowed under this section for any amount paid or incurred in a taxable year ending after the close of 5-year period beginning on the date of the enactment of this section. .\n##### (b) Credit allowed as part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) in the case of an eligible small business, the local media advertising credit determined under section 45BB(a). .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Advertising in local media. .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred in taxable years beginning after the date of the enactment of this Act.\n#### 3. Payroll credit for compensation of local news journalist\n##### (a) In general\nSubchapter D of chapter 21 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n3135. Local news journalist compensation credit (a) In general In the case of an eligible local news journalist employer, there shall be allowed as a credit against applicable employment taxes for each calendar quarter an amount equal to the applicable percentage of the wages paid by such employer to local news journalists for such calendar quarter. (b) Limitations and refundability (1) Limitation on number of local news journalists taken into account The number of employees of any eligible local news journalist employer which are taken into account as local news journalists under subsection (a) for any calendar quarter shall not exceed 1,500. (2) Limitation on wages taken into account The amount of wages paid with respect to any individual which may be taken into account under subsection (a) during any calendar quarter by the eligible local news journalist employer shall not exceed $12,500. (3) Credit limited to employment taxes The credit allowed by subsection (a) with respect to any calendar quarter shall not exceed the applicable employment taxes (reduced by any credits allowed under sections 3131, 3132, and 3134) on the wages paid with respect to the employment of all the employees of the eligible local news journalist employer for such calendar quarter. (4) Refundability of excess credit If the amount of the credit under subsection (a) exceeds the limitation of paragraph (3) for any calendar quarter, such excess shall be treated as an overpayment that shall be refunded under sections 6402(a) and 6413(b). (c) Definitions For purposes of this section\u2014 (1) Applicable percentage The term applicable percentage means\u2014 (A) in the case of each of the first 4 calendar quarters to which this section applies, 50 percent; and (B) in the case of each calendar quarter thereafter, 30 percent. (2) Eligible local news journalist employer The term eligible local news journalist employer means, with respect to any calendar quarter, any employer if substantially all of the gross receipts of such employer for such calendar quarter are derived in the trade or business of publishing local newspapers (as defined in section 45BB(f)). (3) Local news journalist The term local news journalist means, with respect to any eligible local news journalist employer for any calendar quarter, any individual who provides at least 200 hours of service as a local news journalist (as defined in section 45BB(f)(2)) during such calendar quarter to such eligible local news journalist employer. (4) Applicable employment taxes The term applicable employment taxes means the following: (A) The taxes imposed under section 3111(b). (B) So much of the taxes imposed under section 3221(a) as are attributable to the rate in effect under section 3111(b). (d) Aggregation rule (1) In general All persons treated as a single employer under subsection (a) or (b) of section 52 of the Internal Revenue Code of 1986, or subsection (m) or (o) of section 414 of such Code, shall be treated as one employer for purposes of this section. (2) Exception Paragraph (1) shall not apply unless such persons are involved in the production of the same print or digital publication. (e) Certain rules to apply For purposes of this section\u2014 (1) In general Rules similar to the rules of sections 51(i)(1) and 280C(a) of the Internal Revenue Code of 1986 shall apply. (2) Exception to related party rules In the case of an eligible local news journalist employer which employs fewer than 15 local news journalists during the calendar quarter, paragraph (1) shall be applied without regard to the reference to section 51(i)(1). (f) Certain governmental employers This credit shall not apply to the Government of the United States, the government of any State or political subdivision thereof, or any agency or instrumentality of any of the foregoing. (g) Election to have section not apply This section shall not apply with respect to any eligible local news journalist employer for any calendar quarter if such person elects (at such time and in such manner as the Secretary may prescribe) not to have this section apply. (h) Special rules (1) Employee not taken into account more than once An employee shall not be included for purposes of this section for any period with respect to any employer if such employer is allowed a credit under section 51 of the Internal Revenue Code of 1986 with respect to such employee for such period. (2) Denial of double benefit Any wages taken into account in determining the credit allowed under this section shall not be taken into account for purposes of determining the credit allowed under section 41, 45A, 45P, 45S, or 1396. (3) Third-party payors Any credit allowed under this section shall be treated as a credit described in section 3511(d)(2). (4) Treatment of deposits The Secretary shall waive any penalty under section 6656 of the Internal Revenue Code of 1986 for any failure to make a deposit of any applicable employment taxes if the Secretary determines that such failure was due to the reasonable anticipation of the credit allowed under this section. (5) Extension of limitation on assessment Notwithstanding section 6501, the limitation on the time period for the assessment of any amount attributable to a credit claimed under this section shall not expire before the date that is 5 years after the later of\u2014 (A) the date on which the original return which includes the calendar quarter with respect to which such credit is determined is filed, or (B) the date on which such return is treated as filed under section 6501(b)(2). (i) Regulations and guidance The Secretary shall issue such forms, instructions, regulations, and guidance as are necessary\u2014 (1) with respect to the application of the credit under subsection (a) to third-party payors (including professional employer organizations, certified professional employer organizations, or agents under section 3504 of the Internal Revenue Code of 1986), including regulations or guidance allowing such payors to submit documentation necessary to substantiate the eligible employer status of employers that use such payors, and (2) to prevent the avoidance of the purposes of the limitations under this section, including through the leaseback of employees. Any forms, instructions, regulations, or other guidance described in paragraph (2) shall require the customer to be responsible for the accounting of the credit and for any liability for improperly claimed credits and shall require the certified professional employer organization or other third party payor to accurately report such tax credits based on the information provided by the customer. (j) Application This section shall not apply to any calendar quarter beginning more than 5 years after the date of the enactment of this section. .\n##### (b) Conforming amendments\n**(1)**\nSection 1324(b)(2) of title 31, United States Code, is amended by inserting 3135, after 3134, .\n**(2)**\nThe table of sections for subchapter D of chapter 21 of the Internal Revenue Code of 1986 is amended by adding at the end the following:\nSec. 3135. Local news journalist compensation credit. .\n##### (c) Effective date\nThe amendments made by this section shall apply to calendar quarters beginning after the date of the enactment of this Act.",
      "versionDate": "2025-02-27",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-07T16:04:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1753",
          "measure-number": "1753",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2026-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1753v00",
            "update-date": "2026-05-13"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Community News and Small Business Support Act</strong></p><p>This bill establishes a temporary business tax credit for expenses incurred by an eligible small business to advertise in local media. The bill also establishes a temporary refundable tax credit for a percentage of wages paid by an eligible employer to local news journalists. (Limitations apply.)</p><p>Under the bill, an eligible small business (a business with an average of fewer than 50 employees) may claim a tax credit for (1) 80% of local media advertising expenses, up to a maximum of $5,000, in the first year of the tax credit; and (2) 50% of such expenses, up to a maximum of $2,500, in the subsequent four years. (Other conditions and limitations may apply.)</p><p>The bill also allows an eligible employer to claim each calendar quarter a refundable tax credit against Medicare payroll taxes for (1) 50% of wages paid to a local news journalist in the first four calendar quarters of the tax credit, and (2) 30% of such wages paid in each calendar quarter in the subsequent four years.\u00a0</p><p>However, under the bill, the tax credit for local news journalist wages is limited to $12,500 in wages paid per local news journalist per quarter and the wages of no more than 1,500 local news journalists may be included. Further, the tax credit may not be claimed for wages for which certain other tax credits (e.g., the tax credit for paid family and medical leave) are claimed. (Other conditions and limitations may apply.)</p>"
        },
        "title": "Community News and Small Business Support Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1753.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Community News and Small Business Support Act</strong></p><p>This bill establishes a temporary business tax credit for expenses incurred by an eligible small business to advertise in local media. The bill also establishes a temporary refundable tax credit for a percentage of wages paid by an eligible employer to local news journalists. (Limitations apply.)</p><p>Under the bill, an eligible small business (a business with an average of fewer than 50 employees) may claim a tax credit for (1) 80% of local media advertising expenses, up to a maximum of $5,000, in the first year of the tax credit; and (2) 50% of such expenses, up to a maximum of $2,500, in the subsequent four years. (Other conditions and limitations may apply.)</p><p>The bill also allows an eligible employer to claim each calendar quarter a refundable tax credit against Medicare payroll taxes for (1) 50% of wages paid to a local news journalist in the first four calendar quarters of the tax credit, and (2) 30% of such wages paid in each calendar quarter in the subsequent four years.\u00a0</p><p>However, under the bill, the tax credit for local news journalist wages is limited to $12,500 in wages paid per local news journalist per quarter and the wages of no more than 1,500 local news journalists may be included. Further, the tax credit may not be claimed for wages for which certain other tax credits (e.g., the tax credit for paid family and medical leave) are claimed. (Other conditions and limitations may apply.)</p>",
      "updateDate": "2026-05-13",
      "versionCode": "id119hr1753"
    },
    "title": "Community News and Small Business Support Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Community News and Small Business Support Act</strong></p><p>This bill establishes a temporary business tax credit for expenses incurred by an eligible small business to advertise in local media. The bill also establishes a temporary refundable tax credit for a percentage of wages paid by an eligible employer to local news journalists. (Limitations apply.)</p><p>Under the bill, an eligible small business (a business with an average of fewer than 50 employees) may claim a tax credit for (1) 80% of local media advertising expenses, up to a maximum of $5,000, in the first year of the tax credit; and (2) 50% of such expenses, up to a maximum of $2,500, in the subsequent four years. (Other conditions and limitations may apply.)</p><p>The bill also allows an eligible employer to claim each calendar quarter a refundable tax credit against Medicare payroll taxes for (1) 50% of wages paid to a local news journalist in the first four calendar quarters of the tax credit, and (2) 30% of such wages paid in each calendar quarter in the subsequent four years.\u00a0</p><p>However, under the bill, the tax credit for local news journalist wages is limited to $12,500 in wages paid per local news journalist per quarter and the wages of no more than 1,500 local news journalists may be included. Further, the tax credit may not be claimed for wages for which certain other tax credits (e.g., the tax credit for paid family and medical leave) are claimed. (Other conditions and limitations may apply.)</p>",
      "updateDate": "2026-05-13",
      "versionCode": "id119hr1753"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1753ih.xml"
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
      "title": "Community News and Small Business Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community News and Small Business Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide tax incentives that support local media.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T03:03:29Z"
    }
  ]
}
```
