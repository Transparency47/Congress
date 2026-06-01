# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/782?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/782
- Title: Reignite Hope Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 782
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-05-27T18:24:47Z
- Update date including text: 2025-05-27T18:24:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/782",
    "number": "782",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "J000307",
        "district": "10",
        "firstName": "John",
        "fullName": "Rep. James, John [R-MI-10]",
        "lastName": "James",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Reignite Hope Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-27T18:24:47Z",
    "updateDateIncludingText": "2025-05-27T18:24:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:01:45Z",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr782ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 782\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. James (for himself and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a credit for hired critical employees and to make permanent certain expiring provisions relating to the child tax credit.\n#### 1. Short title\nThis Act may be cited as the Reignite Hope Act of 2025 .\n#### 2. Credit for hired critical employees\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25E the following new section:\n25F. Credit for hired critical employees (a) Allowance of credit In the case of a critical employee, there shall be allowed $3,500 as a credit against the tax imposed by this chapter. (b) Critical employee For purposes of this section: (1) In general The term critical employee means any of the following individuals whose employer certifies that such individual worked full-time for not less than 75 percent of the taxable year in such professional capacity and that such individual\u2019s primary place of employment for the majority of hours worked during such taxable year is located in a qualified opportunity zone: (A) A healthcare professional. (B) A law enforcement officer (as such term is defined in section 806 of title I of the Omnibus Crime Control and Safe Streets Act of 1968). (C) A member of a rescue squad or ambulance crew (as such term is defined in section 806 of title I of the Omnibus Crime Control and Safe Streets Act of 1968). (D) A firefighter (as such term is defined in section 806 of title I of the Omnibus Crime Control and Safe Streets Act of 1968). (E) an eligible child care provider or family child care provider (as such terms are defined in section 658P of the Child Care and Development Block Grant Act of 1990). (F) personal or home care aide (as such term is defined in section 2008 of the Social Security Act). (2) Healthcare professional The term healthcare professional means\u2014 (A) a certified nursing assistant, or (B) a licensed practical nurse or registered professional nurse. (3) The term qualified opportunity zone means a census tract designated as a qualified opportunity zone under section 1400z\u20131(b)(1) as of the date of the enactment of this section. (c) Sunset No credit shall be allowed under subsection (a) for any taxable year beginning after the date that is 3 years after the date of the enactment of this section. .\n##### (b) Clerical amendment\nThe table of section for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 25E the following new item:\nSec. 25F. Credit for hired critical employees. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this section.\n#### 3. Permanent extension and modification of special rules for child tax credit\n##### (a) In general\nSection 24 of the Internal Revenue Code of 1986 is amended by striking subsections (a), (b), and (c) and inserting the following new subsections:\n(a) Allowance of credit There shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the sum of\u2014 (1) $3,500 for each qualifying child of the taxpayer ($4,500 in the case of a qualifying child who has not attained age 6 as of the close of the calendar year in which the taxable year of the taxpayer begins), and (2) in the case of any taxable year beginning before January 1, 2026, $500 for each qualifying dependent (other than a qualifying child) of the taxpayer. (b) Limitation based on adjusted gross income The amount of the credit allowable under subsection (a) shall be reduced (but not below zero) by $50 for each $1,000 (or fraction thereof) by which the taxpayer's modified adjusted gross income exceeds $400,000 in the case of a joint return ($200,000 in any other case). For purposes of the preceding sentence, the term \u201cmodified adjusted gross income\u201d means adjusted gross income increased by any amount excluded from gross income under section 911, 931, or 933. (c) Qualifying child; qualifying dependent For purposes of this section\u2014 (1) Qualifying child The term qualifying child means any qualifying dependent of the taxpayer\u2014 (A) who is a qualifying child (as defined in section 152(c)) of the taxpayer, (B) who has not attained age 18 at the close of the calendar year in which the taxable year of the taxpayer begins, and (C) whose name and social security number are included on the taxpayer\u2019s return of tax for the taxable year. (2) Qualifying dependent The term qualifying dependent means any dependent of the taxpayer (as defined in section 152 without regard to all that follows resident of the United States in section 152(b)(3)(A)) whose name and TIN are included on the taxpayer\u2019s return of tax for the taxable year. (3) Social security number defined For purposes of this subsection, the term social security number means, with respect to a return of tax, a social security number issued to an individual by the Social Security Administration, but only if the social security number is issued\u2014 (A) to a citizen of the United States or pursuant to subclause (I) (or that portion of subclause (III) that relates to subclause (I)) of section 205(c)(2)(B)(i) of the Social Security Act, and (B) on or before the due date of filing such return. .\n##### (b) Portion of credit refundable\nSection 24(d)(1) of such Code is amended\u2014\n**(1)**\nby striking subparagraph (A) and inserting the following:\n(A) the credit which would be allowed under this section determined\u2014 (i) without regard to subsection (a)(2), and (ii) without regard to this subsection (other than this subparagraph) and the limitation under section 26(a), or , and\n**(2)**\nin subparagraph (B)(i), by striking 15 percent of so much of the taxpayer's earned income (within the meaning of section 32) which is taken into account in computing taxable income for the taxable year as exceeds $3,000 and inserting 15.3 percent of the taxpayer's earned income (within the meaning of section 32) which is taken into account in computing taxable income .\n##### (c) Conforming amendments\n**(1)**\nSection 24(e) of such Code is amended to read as follows:\n(e) Taxpayer identification requirement No credit shall be allowed under this section if the identifying number of the taxpayer was issued after the due date for filing the return of tax for the taxable year. .\n**(2)**\nSection 24 of such Code is amended by striking subsection (h).\n##### (d) Removal of deadwood\n**(1)**\nSection 24 of such Code is amended by striking subsections (i), (j), and (k).\n**(2)**\nChapter 77 of such Code is amended by striking section 7527A (and by striking the item relating to section 7527A in the table of sections for such chapter).\n**(3)**\nSection 26(b)(2) of such Code is amended by inserting and at the end of subparagraph (X), by striking , and at the end of subparagraph (Y) and inserting a period, and by striking subparagraph (Z).\n**(4)**\nSection 3402(f)(1)(C) of such Code is amended by striking section 24 (determined after application of subsection (j) thereof) and inserting section 24(a) .\n**(5)**\nSection 6211(b)(4)(A) of such Code is amended\u2014\n**(A)**\nby striking 24 by reason of subsections (d) and (i)(1) thereof and inserting 24(d) , and\n**(B)**\nby striking 6428B, and 7527A and inserting and 6428B .\n**(6)**\nSection 1324(b)(2) of title 31, United States Code, is amended by striking 6431, or 7527A and inserting or 6431 .\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-01-28",
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
        "updateDate": "2025-04-02T14:28:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr782",
          "measure-number": "782",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-05-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr782v00",
            "update-date": "2025-05-27"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Reignite Hope Act of 2025 </strong></p><p>This bill establishes a new nonrefundable personal tax credit (for three years) of $3,500 for critical employees. The bill also increases and makes other changes to the child tax credit.</p><p>Under the bill, a <em>critical employee</em> is defined as an individual who works full-time for at least 75% of the tax year (as certified by such individual\u2019s employer) as a</p><ul><li>healthcare professional,</li><li>law enforcement officer,</li><li>member of a rescue squad or ambulance crew,</li><li>firefighter,</li><li>eligible child care provider,</li><li>family child care provider, or</li><li>personal or homecare aid.</li></ul><p>Further, under the bill, such individual\u2019s primary place of employment for the majority of hours worked during the tax year must be in a qualified opportunity zone. (A qualified opportunity zone is an economically distressed community where new investments may be eligible for certain tax preferences.)</p><p>This bill increases the child tax credit from $2,000 per qualifying child to $3,500 per qualifying child (or $4,500 per qualifying child under six years old).</p><p>The bill also</p><ul><li>increases the age limit of a qualifying child to 17 years old (from 16 years old),</li><li>extends the\u00a0threshold at which the child tax credit begins to phase out ($200,000 for single taxpayers or $400,000 for married taxpayers filing jointly),</li><li>extends the child tax credit identification requirements applicable to qualifying children, and</li><li>increases the refundable portion of the child tax credit for certain taxpayers with fewer than three qualifying children.</li></ul>"
        },
        "title": "Reignite Hope Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr782.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reignite Hope Act of 2025 </strong></p><p>This bill establishes a new nonrefundable personal tax credit (for three years) of $3,500 for critical employees. The bill also increases and makes other changes to the child tax credit.</p><p>Under the bill, a <em>critical employee</em> is defined as an individual who works full-time for at least 75% of the tax year (as certified by such individual\u2019s employer) as a</p><ul><li>healthcare professional,</li><li>law enforcement officer,</li><li>member of a rescue squad or ambulance crew,</li><li>firefighter,</li><li>eligible child care provider,</li><li>family child care provider, or</li><li>personal or homecare aid.</li></ul><p>Further, under the bill, such individual\u2019s primary place of employment for the majority of hours worked during the tax year must be in a qualified opportunity zone. (A qualified opportunity zone is an economically distressed community where new investments may be eligible for certain tax preferences.)</p><p>This bill increases the child tax credit from $2,000 per qualifying child to $3,500 per qualifying child (or $4,500 per qualifying child under six years old).</p><p>The bill also</p><ul><li>increases the age limit of a qualifying child to 17 years old (from 16 years old),</li><li>extends the\u00a0threshold at which the child tax credit begins to phase out ($200,000 for single taxpayers or $400,000 for married taxpayers filing jointly),</li><li>extends the child tax credit identification requirements applicable to qualifying children, and</li><li>increases the refundable portion of the child tax credit for certain taxpayers with fewer than three qualifying children.</li></ul>",
      "updateDate": "2025-05-27",
      "versionCode": "id119hr782"
    },
    "title": "Reignite Hope Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reignite Hope Act of 2025 </strong></p><p>This bill establishes a new nonrefundable personal tax credit (for three years) of $3,500 for critical employees. The bill also increases and makes other changes to the child tax credit.</p><p>Under the bill, a <em>critical employee</em> is defined as an individual who works full-time for at least 75% of the tax year (as certified by such individual\u2019s employer) as a</p><ul><li>healthcare professional,</li><li>law enforcement officer,</li><li>member of a rescue squad or ambulance crew,</li><li>firefighter,</li><li>eligible child care provider,</li><li>family child care provider, or</li><li>personal or homecare aid.</li></ul><p>Further, under the bill, such individual\u2019s primary place of employment for the majority of hours worked during the tax year must be in a qualified opportunity zone. (A qualified opportunity zone is an economically distressed community where new investments may be eligible for certain tax preferences.)</p><p>This bill increases the child tax credit from $2,000 per qualifying child to $3,500 per qualifying child (or $4,500 per qualifying child under six years old).</p><p>The bill also</p><ul><li>increases the age limit of a qualifying child to 17 years old (from 16 years old),</li><li>extends the\u00a0threshold at which the child tax credit begins to phase out ($200,000 for single taxpayers or $400,000 for married taxpayers filing jointly),</li><li>extends the child tax credit identification requirements applicable to qualifying children, and</li><li>increases the refundable portion of the child tax credit for certain taxpayers with fewer than three qualifying children.</li></ul>",
      "updateDate": "2025-05-27",
      "versionCode": "id119hr782"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr782ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to establish a credit for hired critical employees and to make permanent certain expiring provisions relating to the child tax credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T06:03:38Z"
    },
    {
      "title": "Reignite Hope Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reignite Hope Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:53:20Z"
    }
  ]
}
```
