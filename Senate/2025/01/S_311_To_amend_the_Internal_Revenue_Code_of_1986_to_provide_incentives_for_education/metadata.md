# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/311?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/311
- Title: ACE Act
- Congress: 119
- Bill type: S
- Bill number: 311
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-12-05T21:32:58Z
- Update date including text: 2025-12-05T21:32:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/311",
    "number": "311",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "ACE Act",
    "type": "S",
    "updateDate": "2025-12-05T21:32:58Z",
    "updateDateIncludingText": "2025-12-05T21:32:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
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
      "actionDate": "2025-01-29",
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
          "date": "2025-01-29T20:29:23Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "NC"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s311is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 311\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Lee (for himself and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide incentives for education.\n#### 1. Short title\nThis Act may be cited as the Achieving Choice in Education Act or the ACE Act .\n#### 2. 529 account funding for homeschool and additional elementary and secondary expenses\n##### (a) In general\nSection 529(c)(7) of the Internal Revenue Code of 1986 is amended to read as follows:\n(7) Treatment of elementary and secondary tuition Any reference in this section to the term qualified higher education expense shall include a reference to the following expenses in connection with enrollment or attendance at, or for students enrolled at or attending, an elementary or secondary public, private, or religious school: (A) Tuition. (B) Curriculum and curricular materials. (C) Books or other instructional materials. (D) Online educational materials. (E) Tuition for tutoring or educational classes outside of the home, including at a tutoring facility, but only if the tutor or instructor is not related to the student and\u2014 (i) is licensed as a teacher in any State, (ii) has taught at an eligible educational institution, or (iii) is a subject matter expert in the relevant subject. (F) Fees for a nationally standardized norm-referenced achievement test, an advanced placement examination, or any examinations related to college or university admission. (G) Fees for dual enrollment in an institution of higher education. (H) Educational therapies for students with disabilities provided by a licensed or accredited practitioner or provider, including occupational, behavioral, physical, and speech-language therapies. Such term shall include expenses for the purposes described in subparagraphs (A) through (H) in connection with a homeschool (whether treated as a homeschool or a private school for purposes of applicable State law). .\n##### (b) Effective date\nThe amendment made by this section shall apply to distributions made after the date of the enactment of this Act.\n#### 3. Increase in limitation on distributions from 529 plans for elementary and secondary school expenses\n##### (a) In general\nSection 529(e)(3)(A) of the Internal Revenue Code of 1986 is amended by striking $10,000 in the flush matter at the end and inserting $20,000 .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2026.\n#### 4. Gift tax exclusions\n##### (a) Gift tax exclusion for contributions to 529 plans\nSection 2503(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(3) Exclusion for contributions to 529 plans The dollar amount in effect under paragraph (1) with respect to gifts (to which such paragraph applies) made to any person during any calendar year shall be increased (not in excess of $20,000) by the amount of such gifts made during such calendar year to qualified tuition programs (as defined in section 529) with respect to which such person is the designated beneficiary. .\n##### (b) Effective date\nThe amendments made by this section shall apply to gifts made after December 31, 2026.\n#### 5. Tax-exempt bonds restricted to States that implement school choice laws\n##### (a) In general\nSection 103 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(d) Restriction to States that implement school choice laws (1) In general Subsection (a) shall not apply to any State or local bond unless such bond is issued by a minimum school choice State or a political subdivision of such a State. (2) Partial exclusion with respect to certain States (A) In general In the case of any State or local bond issued by a minimum school choice State which does not meet the requirements of subparagraph (B) (or issued by any political subdivision of such a State), subsection (a) shall be applied by substituting 50 percent of the interest for interest . (B) Requirements A minimum school choice State meets the requirements of this subparagraph if the Secretary determines that\u2014 (i) at least 65 percent of the specified school age children are eligible for one or more of such State\u2019s school choice programs, and (ii) the average amount spent by such State on the education of each specified school age child eligible for one or more of such State\u2019s school choice programs is at least 75 percent of the average amount spent by such State on the education of each specified school age child not eligible for one or more of such programs. (3) Minimum school choice State For purposes of this subsection, the term minimum school choice State means any State if the Secretary determines that\u2014 (A) such State has enacted one or more school choice programs, (B) at least 40 percent of the specified school age children are eligible for one or more of such State\u2019s school choice programs, and (C) the average amount spent by such State on the education of each specified school age child eligible for one or more of such State\u2019s school choice programs is at least 60 percent of the average amount spent by such State on the education of each specified school age child not eligible for one or more of such programs. (4) School choice programs For purposes of this subsection, the term school choice program means, with respect to any State, each of the following with respect to elementary and secondary education in such State: (A) Tax credit scholarship programs. (B) Voucher programs. (C) Education savings account program. (D) Refundable tax credit for private education expenses. (5) Specified school age child For purposes of this subsection, the term specified school age child means, with respect to any State, any individual residing in such State who has not attained age 18. .\n##### (b) Effective date\nThe amendment made by this section shall apply to bonds issued after the date of the enactment of this Act.",
      "versionDate": "2025-01-29",
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
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "939",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Student Empowerment Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-20",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "152",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Student Empowerment Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "750",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ACE Act",
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
        "updateDate": "2025-04-28T21:51:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
    "originChamber": "Senate",
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
          "measure-id": "id119s311",
          "measure-number": "311",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-05-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s311v00",
            "update-date": "2025-05-02"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Achieving Choice in Education Act or the ACE Act</strong></p><p>This bill expands the expenses that may be paid for with tax-free distributions from a qualified tuition program (known as a 529 plan) to include certain elementary, secondary, and homeschool education\u00a0expenses and makes other changes related to 529 plans. The bill also limits the tax exclusion\u00a0for interest on state or local bonds.</p><p>Under current law, 529 plan distributions are excluded from gross income if they are used to pay for qualified higher education expenses, which includes up to $10,000 (per year and per beneficiary) for tuition at an elementary or secondary public, private, or religious school.</p><p>The bill expands the expenses that may be paid for with tax-free 529 plan distributions to include homeschooling tuition and the following expenses related to elementary, secondary, and homeschool education:</p><ul><li>curriculum,</li><li>books,</li><li>instructional and online educational materials,</li><li>tutoring or educational classes outside the home,</li><li>testing fees,</li><li>fees for dual enrollment in a\u00a0higher education institution, and</li><li>educational therapies for disabled\u00a0students.</li></ul><p>The bill also increases the amount of tax-free 529 plan distributions that may be used to pay for elementary, secondary, and homeschool education expenses to $20,000.</p><p>The bill increases the annual gift tax exclusion by $20,000 for contributions made to a 529 plan. (Under current law, up to $19,000 may be excluded from taxable gifts in 2025.)</p><p>Finally, the bill limits the tax exclusion for interest on state or local bonds to bonds issued by\u00a0states that meet minimum school choice requirements or political subdivisions of such states.</p>"
        },
        "title": "ACE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s311.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Achieving Choice in Education Act or the ACE Act</strong></p><p>This bill expands the expenses that may be paid for with tax-free distributions from a qualified tuition program (known as a 529 plan) to include certain elementary, secondary, and homeschool education\u00a0expenses and makes other changes related to 529 plans. The bill also limits the tax exclusion\u00a0for interest on state or local bonds.</p><p>Under current law, 529 plan distributions are excluded from gross income if they are used to pay for qualified higher education expenses, which includes up to $10,000 (per year and per beneficiary) for tuition at an elementary or secondary public, private, or religious school.</p><p>The bill expands the expenses that may be paid for with tax-free 529 plan distributions to include homeschooling tuition and the following expenses related to elementary, secondary, and homeschool education:</p><ul><li>curriculum,</li><li>books,</li><li>instructional and online educational materials,</li><li>tutoring or educational classes outside the home,</li><li>testing fees,</li><li>fees for dual enrollment in a\u00a0higher education institution, and</li><li>educational therapies for disabled\u00a0students.</li></ul><p>The bill also increases the amount of tax-free 529 plan distributions that may be used to pay for elementary, secondary, and homeschool education expenses to $20,000.</p><p>The bill increases the annual gift tax exclusion by $20,000 for contributions made to a 529 plan. (Under current law, up to $19,000 may be excluded from taxable gifts in 2025.)</p><p>Finally, the bill limits the tax exclusion for interest on state or local bonds to bonds issued by\u00a0states that meet minimum school choice requirements or political subdivisions of such states.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s311"
    },
    "title": "ACE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Achieving Choice in Education Act or the ACE Act</strong></p><p>This bill expands the expenses that may be paid for with tax-free distributions from a qualified tuition program (known as a 529 plan) to include certain elementary, secondary, and homeschool education\u00a0expenses and makes other changes related to 529 plans. The bill also limits the tax exclusion\u00a0for interest on state or local bonds.</p><p>Under current law, 529 plan distributions are excluded from gross income if they are used to pay for qualified higher education expenses, which includes up to $10,000 (per year and per beneficiary) for tuition at an elementary or secondary public, private, or religious school.</p><p>The bill expands the expenses that may be paid for with tax-free 529 plan distributions to include homeschooling tuition and the following expenses related to elementary, secondary, and homeschool education:</p><ul><li>curriculum,</li><li>books,</li><li>instructional and online educational materials,</li><li>tutoring or educational classes outside the home,</li><li>testing fees,</li><li>fees for dual enrollment in a\u00a0higher education institution, and</li><li>educational therapies for disabled\u00a0students.</li></ul><p>The bill also increases the amount of tax-free 529 plan distributions that may be used to pay for elementary, secondary, and homeschool education expenses to $20,000.</p><p>The bill increases the annual gift tax exclusion by $20,000 for contributions made to a 529 plan. (Under current law, up to $19,000 may be excluded from taxable gifts in 2025.)</p><p>Finally, the bill limits the tax exclusion for interest on state or local bonds to bonds issued by\u00a0states that meet minimum school choice requirements or political subdivisions of such states.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s311"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s311is.xml"
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
      "title": "ACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Achieving Choice in Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide incentives for education.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:49Z"
    }
  ]
}
```
