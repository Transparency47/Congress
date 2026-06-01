# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1308?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1308
- Title: FISC Act
- Congress: 119
- Bill type: HR
- Bill number: 1308
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-04-20T14:53:57Z
- Update date including text: 2026-04-20T14:53:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1308",
    "number": "1308",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000592",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Golden, Jared F. [D-ME-2]",
        "lastName": "Golden",
        "party": "D",
        "state": "ME"
      }
    ],
    "title": "FISC Act",
    "type": "HR",
    "updateDate": "2026-04-20T14:53:57Z",
    "updateDateIncludingText": "2026-04-20T14:53:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:05:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1308ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1308\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Golden of Maine introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide monthly payments for eligible pregnant women and parents to improve the ability of families to provide for their children and other family members, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Family Income Supplemental Credit Act or the FISC Act .\n#### 2. Family income supplements\n##### (a) Applications\n**(1) In general**\n**(A) Qualified pregnant woman**\nA pregnant woman may apply to the Commissioner of Social Security (in this section referred to as the Commissioner ) for monthly payments under this section with respect to the pregnancy.\n**(B) Qualified caregiver**\nA qualified caregiver of an eligible child may apply to the Commissioner for monthly payments under this section with respect to the eligible child.\n**(2) Contents**\nThe application shall contain the following:\n**(A) Pregnant woman**\n**(i) In general**\nAn application submitted pursuant to paragraph (1)(A) shall contain\u2014\n**(I)**\nthe name, residential address, and social security account or tax identification number of the applicant;\n**(II)**\nthe expected due date of the birth;\n**(III)**\nthe name and address of the person who is providing pre-natal care with respect to the pregnancy;\n**(IV)**\na specification of the income of the applicant for the then most recently ended taxable year of the applicant; and\n**(V)**\na statement as to whether the applicant is married.\n**(ii) Beginning of pregnancy**\nFor purposes of this section, the date a pregnancy began shall be determined on the basis commonly used by licensed physicians.\n**(B) Qualified caregiver**\nAn application submitted pursuant to paragraph (1)(B) shall contain\u2014\n**(i)**\nthe name and residential address of the child and of each qualified caregiver of the child;\n**(ii)**\nthe age of the child;\n**(iii)**\nthe social security account or tax identification number of the child;\n**(iv)**\nthe social security account number or tax identification number of each qualified caregiver of the child;\n**(v)**\na specification of the income of the applicant for the then most recently ended taxable year of the applicant; and\n**(vi)**\na statement as to whether the applicant is married.\n##### (b) Definitions\nIn this section:\n**(1) Eligible child**\nThe term eligible child means an individual who\u2014\n**(A)**\nhas not attained 18 years of age;\n**(B)**\nhas provided not more than half of their own financial support during the most recent taxable year of the child; and\n**(C)**\nis a citizen or national of the United States, or a permanent resident alien.\n**(2) Qualified caregiver**\n**(A) In general**\nThe term qualified caregiver means, with respect to a child, an individual who\u2014\n**(i)**\nhas attained 18 years of age;\n**(ii)**\nresides with the child; and\n**(iii)**\nprovides economic support for the child.\n**(B) Fraud disqualification**\nNotwithstanding subparagraph (A), the term qualified caregiver does not include an individual if\u2014\n**(i)**\nthe Commissioner, after notice and an opportunity for hearing, finds that the individual committed fraud in relation to the program under this section; and\n**(ii)**\nthe finding has not been reversed or vacated by a court of law.\n##### (c) Entitlement\nOn approval by the Commissioner of an application submitted pursuant to subsection (a), the applicant shall become a beneficiary entitled to monthly payments under this section\u2014\n**(1)**\nfor the calendar month in which the application is so submitted and each subsequent calendar month, if at any time in the month the beneficiary is a pregnant woman whose pregnancy has lasted for at least 20 weeks; and\n**(2)**\nfor each calendar month after the calendar month in which an eligible child is born, in which the beneficiary is a qualified caregiver of the eligible child.\n##### (d) Amount of monthly payment\n**(1) In general**\n**(A) With respect to a pregnancy**\nThe amount of the monthly payment to a beneficiary under this section with respect to a pregnancy shall be $800.\n**(B) With respect to an eligible child**\nThe amount of the monthly payment to a beneficiary under this section with respect to each eligible child shall be\u2014\n**(i)**\n$400, if the child has not attained 6 years of age; or\n**(ii)**\n$250, if the child has attained 6 years of age.\n**(2) Marriage bonus**\nThe total amount of the monthly payment to a beneficiary under paragraph (1) shall be increased by 20 percent if the beneficiary is\u2014\n**(A)**\na married pregnant woman; or\n**(B)**\nmarried to a qualified caregiver of an eligible child of the beneficiary.\n**(3) Phase-out**\nThe total amount of the monthly payment to a beneficiary under the preceding provisions of this subsection shall be decreased (but not below zero) by $16.67 for each whole $1,000 by which\u2014\n**(A)**\nthe adjusted gross income of the beneficiary for the then most recently ended taxable year of the beneficiary exceeds $125,000; or\n**(B)**\nif the beneficiary and the spouse of the beneficiary filed a joint return of Federal income tax for that taxable year, the total adjusted gross income of the beneficiary and the spouse of the beneficiary for the taxable year exceeds $250,000.\n**(4) Limitation**\nThe total amount of the monthly payment to a beneficiary under the preceding provisions of this subsection shall not exceed 1/12 of the total adjusted gross income of the beneficiary and the spouse (if any) of the beneficiary for the then most recently ended taxable year of the beneficiary.\n##### (e) Recipient of payment\nThe Commissioner may make payments under the preceding provisions of this section with respect to an eligible child to only 1 qualified caregiver of the eligible child.\n##### (f) Provisional continuation of benefits for limited period in certain cases\nIn the case of a beneficiary under this section with respect to a pregnancy that results in the birth of a child\u2014\n**(1)**\nthe entitlement of the beneficiary with respect to the pregnancy is deemed to be converted into an entitlement to benefits under this section with respect to the child, subject to the submission by a qualified caregiver of the child, within 90 days after the birth, of an application pursuant to subsection (a)(1)(B) and the approval by the Commissioner of the application; and\n**(2)**\nthe Commissioner\u2014\n**(A)**\nshall ensure that benefit payments under this section to a qualified caregiver of the child are not interrupted during that 90-day period; and\n**(B)**\nmay not seek to recover any benefit payment made under this section to a qualified caregiver of the child on account of the entitlement with respect to the child, if such a qualified caregiver does not submit such an application within that 90-day period or an application so submitted is disapproved.\n##### (g) Administrative provisions\n**(1) Bureau of Family Statistics**\nThere is established in the Social Security Administration the Bureau of Family Statistics (in this section referred to as the Bureau ).\n**(2) Duties**\nThe Bureau shall gather and provide to the Commissioner such statistical purpose (as defined in section 3561 of title 44, United States Code) information as is necessary to enable the Commissioner to carry out this section.\n##### (h) Regulations\n**(1) In general**\nThe Commissioner shall prescribe such regulations as are necessary to carry out this section.\n**(2) System for reporting change in status**\nThe Commissioner shall develop and implement a system to allow an applicant or beneficiary pursuant to this section to report a change in the marital or caregiver status of the applicant or beneficiary.\n##### (i) Annual reports\nThe Commissioner shall prepare and submit to the Congress annual reports on the activities undertaken under this section. Each such report shall, with respect to the then most recently completed calendar year\u2014\n**(1)**\nspecify the average length of time from the date the Commissioner received an application submitted pursuant to this section with respect to a pregnancy or an eligible child to the date the 1st payment is made under this section with respect to the pregnancy or the eligible child;\n**(2)**\ninclude recommendations to reduce the average; and\n**(3)**\nspecify the total of the amounts paid under this section in the calendar year.\n##### (j) Appropriation\nOut of any amounts in the Treasury of the United States not otherwise appropriated, there are appropriated such sums as are necessary to carry out this section.\n##### (k) Effective date\nThis section shall take effect on the 1st day of the 1st calendar month that begins 1 year or more after the date of the enactment of this section.\n#### 3. Repeal of child tax credit\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by striking section 24 (and by striking the item relating to such section in the table of sections for such subpart).\n##### (b) Conforming amendments\n**(1)**\nSection 26(b)(2) of such Code is amended by striking subparagraph (Z).\n**(2)**\nSection 45R(f)(3)(B) of such Code is amended to read as follows:\n(B) Special rule Any amounts paid pursuant to an agreement under section 3121(l) (relating to agreements entered into by American employers with respect to foreign affiliates) which are equivalent to the taxes referred to in subparagraph (A) shall be treated as taxes referred to in such subparagraph. .\n**(3)**\nSection 48D(d)(4) of such Code is amended\u2014\n**(A)**\nby striking possessions.\u2014 In the case of and inserting the following:\npossessions .\u2014 (A) In general In the case of ,\n**(B)**\nby striking (as defined in section 24(k) , and\n**(C)**\nby adding at the end the following new subparagraph:\n(B) Mirror code tax system For purposes of this paragraph, the term mirror code tax system means, with respect to any possession of the United States, the income tax system of such possession if the income tax liability of the residents of such possession under such system is determined by reference to the income tax laws of the United States as if such possession were the United States. .\n**(4)**\nSection 152(f)(6)(B) of such Code is amended by striking clause (ii).\n**(5)**\nThe second sentence of section 501(c)(26) of such Code is amended\u2014\n**(A)**\nby striking (as defined in section 24(c)) , and\n**(B)**\nby adding at the end the following: For purposes of the preceding sentence, the term qualifying child has the meaning given such term by section 152(c), except such term shall not include any individual who has attained the age of 17 or who would not be a dependent if subparagraph (A) of section 152(b)(3) were applied without regard to all that follows resident of the United States . .\n**(6)**\nSection 3402(f)(1) of such Code is amended by striking subparagraph (C).\n**(7)**\nSection 6402(m) of such Code is amended by striking section 24 (by reason of subsection (d) thereof) or .\n**(8)**\nSection 6211(b)(4)(A) of such Code is amended by striking 24 by reason of subsections (d) and (i)(1) thereof, .\n**(9)**\nSection 6417(f) of such Code is amended by striking (as defined in section 24(k)) and inserting (as defined in section 48D(d)(4)(B)) .\n**(10)**\n**(A)**\nChapter 77 of such Code is amended by striking section 7527A (and by striking the item relating to such section in the table of sections for such chapter).\n**(B)**\nSection 6211(b)(4)(A) of such Code is amended by striking 7527A, .\n**(11)**\nSection 6213(g)(2) of such Code is amended by striking subparagraphs (I) and (P).\n**(12)**\nSection 6695(g)(2) of such Code is amended by striking 24, .\n**(13)**\nSection 1324(b)(2) of title 31, United States Code, is amended by striking , 24 .\n##### (c) Effective date\n**(1) In general**\nThe amendments made by this section shall apply to taxable years beginning after the first taxable year during which the 1st calendar month described in section 2(l) begins.\n**(2) Transition rule**\nIn the case of any such first taxable year which does not begin with such 1st calendar month, the credit otherwise determined under section 24 of the Internal Revenue Code of 1986 shall be reduced to an amount which bears the same ratio to the amount of such credit (determined without regard to this paragraph) as\u2014\n**(A)**\nthe number of calendar months ending during such taxable year before such 1st calendar month, bears to\n**(B)**\n12.",
      "versionDate": "2025-02-13",
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
        "updateDate": "2025-05-06T17:48:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1308",
          "measure-number": "1308",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2026-04-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1308v00",
            "update-date": "2026-04-20"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Family Income Supplemental Credit Act or the FISC Act</strong></p><p>This bill replaces the federal child tax credit with monthly payments provided by the Social Security Administration (SSA)\u00a0to qualified pregnant women and caregivers of\u00a0eligible children.</p><p>Specifically, the bill provides a monthly payment of</p><ul><li>$800 to a qualified pregnant woman,</li><li>$400 to a qualified caregiver for each eligible child who is under six years old, and</li><li>$250 to a qualified caregiver for each eligible child who is at least\u00a0six years old.</li></ul><p>The monthly payment increases by 20% if the individual is a married pregnant woman or married to a qualified caregiver of an eligible child.</p><p>Under the bill, the monthly payment begins to phase out for individuals with an adjusted gross income exceeding $125,000 ($250,000 for joint filers) for the most recently ended tax year. (Other limitations apply.)</p><p>The bill defines an <em>eligible child</em> as an individual who</p><ul><li>is under 18 years old;</li><li>is a U.S. citizen, U.S. national, or permanent resident alien; and</li><li>does not provide more than half of their own financial\u00a0support during the tax year.</li></ul><p>Further, a qualified caregiver must be at least 18 years old, reside with the child, and economically support the child.</p><p>The bill also provides funding for the monthly payments and establishes the Bureau of Family Statistics within the SSA to provide certain information.</p><p>Finally, the bill requires the SSA to issue regulations, establish a system to report marital or caregiver status changes, and report to Congress annually on the payments.</p>"
        },
        "title": "FISC Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1308.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Family Income Supplemental Credit Act or the FISC Act</strong></p><p>This bill replaces the federal child tax credit with monthly payments provided by the Social Security Administration (SSA)\u00a0to qualified pregnant women and caregivers of\u00a0eligible children.</p><p>Specifically, the bill provides a monthly payment of</p><ul><li>$800 to a qualified pregnant woman,</li><li>$400 to a qualified caregiver for each eligible child who is under six years old, and</li><li>$250 to a qualified caregiver for each eligible child who is at least\u00a0six years old.</li></ul><p>The monthly payment increases by 20% if the individual is a married pregnant woman or married to a qualified caregiver of an eligible child.</p><p>Under the bill, the monthly payment begins to phase out for individuals with an adjusted gross income exceeding $125,000 ($250,000 for joint filers) for the most recently ended tax year. (Other limitations apply.)</p><p>The bill defines an <em>eligible child</em> as an individual who</p><ul><li>is under 18 years old;</li><li>is a U.S. citizen, U.S. national, or permanent resident alien; and</li><li>does not provide more than half of their own financial\u00a0support during the tax year.</li></ul><p>Further, a qualified caregiver must be at least 18 years old, reside with the child, and economically support the child.</p><p>The bill also provides funding for the monthly payments and establishes the Bureau of Family Statistics within the SSA to provide certain information.</p><p>Finally, the bill requires the SSA to issue regulations, establish a system to report marital or caregiver status changes, and report to Congress annually on the payments.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119hr1308"
    },
    "title": "FISC Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Family Income Supplemental Credit Act or the FISC Act</strong></p><p>This bill replaces the federal child tax credit with monthly payments provided by the Social Security Administration (SSA)\u00a0to qualified pregnant women and caregivers of\u00a0eligible children.</p><p>Specifically, the bill provides a monthly payment of</p><ul><li>$800 to a qualified pregnant woman,</li><li>$400 to a qualified caregiver for each eligible child who is under six years old, and</li><li>$250 to a qualified caregiver for each eligible child who is at least\u00a0six years old.</li></ul><p>The monthly payment increases by 20% if the individual is a married pregnant woman or married to a qualified caregiver of an eligible child.</p><p>Under the bill, the monthly payment begins to phase out for individuals with an adjusted gross income exceeding $125,000 ($250,000 for joint filers) for the most recently ended tax year. (Other limitations apply.)</p><p>The bill defines an <em>eligible child</em> as an individual who</p><ul><li>is under 18 years old;</li><li>is a U.S. citizen, U.S. national, or permanent resident alien; and</li><li>does not provide more than half of their own financial\u00a0support during the tax year.</li></ul><p>Further, a qualified caregiver must be at least 18 years old, reside with the child, and economically support the child.</p><p>The bill also provides funding for the monthly payments and establishes the Bureau of Family Statistics within the SSA to provide certain information.</p><p>Finally, the bill requires the SSA to issue regulations, establish a system to report marital or caregiver status changes, and report to Congress annually on the payments.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119hr1308"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1308ih.xml"
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
      "title": "FISC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T09:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FISC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T09:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Family Income Supplemental Credit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T09:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide monthly payments for eligible pregnant women and parents to improve the ability of families to provide for their children and other family members, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T09:03:25Z"
    }
  ]
}
```
