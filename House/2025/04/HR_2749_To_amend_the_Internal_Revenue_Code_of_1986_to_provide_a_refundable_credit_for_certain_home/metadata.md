# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2749?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2749
- Title: To amend the Internal Revenue Code of 1986 to provide a refundable credit for certain home accessibility improvements.
- Congress: 119
- Bill type: HR
- Bill number: 2749
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2025-12-05T22:52:10Z
- Update date including text: 2025-12-05T22:52:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-04-08 - IntroReferral: Sponsor introductory remarks on measure. (CR H1498)
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-04-08 - IntroReferral: Sponsor introductory remarks on measure. (CR H1498)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2749",
    "number": "2749",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to provide a refundable credit for certain home accessibility improvements.",
    "type": "HR",
    "updateDate": "2025-12-05T22:52:10Z",
    "updateDateIncludingText": "2025-12-05T22:52:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1498)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:01:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2749ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2749\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Ms. Stevens introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a refundable credit for certain home accessibility improvements.\n#### 1. Refundable tax credit for certain home accessibility improvements\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n36C. Credit for certain home accessibility improvements (a) In general In the case of an individual, there shall be allowed as a credit against the tax imposed by this subtitle for any taxable year an amount equal to 35 percent of the qualified home accessibility improvement expenditures paid or incurred during such taxable year with respect to a qualified individual. (b) Limitations (1) Dollar limitations The aggregate amount of qualified home accessibility improvement expenditures taken into account under subsection (a) shall not exceed\u2014 (A) $10,000 for any taxable year, and (B) $30,000 for all taxable years. (2) Income limitation (A) In general The amount allowable as a credit under subsection (a) for any taxable year shall be reduced (but not below zero) by an amount which bears the same ratio to the amount so allowable (determined without regard to this paragraph but after the application of paragraph (1)) as\u2014 (i) the amount (if any) by which the taxpayer\u2019s modified adjusted gross income exceeds the applicable threshold amount, bears to (ii) the applicable phaseout amount. (B) Applicable threshold amount For purposes of this paragraph, the term applicable threshold amount means, with respect to any taxpayer\u2014 (i) $400,000, in the case of a joint return or surviving spouse (as defined in section 2), (ii) $200,000, in the case of a head of household, and (iii) $200,000, in any other case. (C) Applicable phaseout amount For purposes of this paragraph, the term applicable phaseout amount means, with respect to any taxpayer\u2014 (i) $100,000, in the case of a joint return or surviving spouse (as defined in section 2), (ii) $75,000, in the case of a head of household, and (iii) $50,000, in any other case. (D) Modified adjusted gross income For purposes of this paragraph, the term modified adjusted gross income means adjusted gross income determined without regard to sections 911, 931, and 933. (c) Qualified individual For purposes of this section\u2014 (1) In general The term qualified individual means, with respect to an individual for any taxable year\u2014 (A) such individual if such individual\u2014 (i) is, at any time during such taxable year, entitled, based on blindness or disability, to\u2014 (I) pension benefits under title 38, United States Code, or (II) benefits under title II or XVI of the Social Security Act, (ii) has a disability certification filed with the Secretary for such taxable year, or (iii) has (as of the close of such taxable year) attained age 60, and (B) the spouse or any dependent of such individual if such spouse or dependent\u2014 (i) meets the requirements of clause (i), (ii), or (iii) of subparagraph (A), and (ii) has the same principal place of abode as such individual. (2) Disability certification (A) In general The term disability certification means, with respect to an individual, a certification to the satisfaction of the Secretary by a physician meeting the criteria of section 1861(r)(1) of the Social Security Act that\u2014 (i) certifies that the individual\u2014 (I) has a medically determinable physical or mental impairment, which results in marked and severe functional limitations, and which can be expected to result in death or which has lasted or can be expected to last for a continuous period of not less than 12 months, or (II) is blind (within the meaning of section 1614(a)(2) of the Social Security Act), and (ii) includes a copy of the individual\u2019s diagnosis relating to the individual's relevant impairment or impairments, signed by such physician. (B) Restriction on use of certification No inference may be drawn from a disability certification for purposes of establishing eligibility for benefits under title II, XVI, or XIX of the Social Security Act. (d) Qualified home accessibility improvement expenditures For purposes of this section\u2014 (1) In general The term qualified home accessibility improvement expenditures means reasonable amounts paid or incurred by the taxpayer to make qualified improvements to the taxpayer\u2019s principal place of abode for the purpose of making such place of abode more accessible to a qualified individual with respect to the taxpayer. (2) Qualified improvements The term qualified improvements means\u2014 (A) the installation of entrance and exit ramps to create a no-step entry, or modification of areas in front of entry and exit doorways including grading of the ground to provide access to the residence, (B) the installation of handrails or grab bars, including in bathrooms, and other modifications to bathrooms including curbless-entry showers and roll-under sinks, (C) the widening of exterior or interior doorways or hallways, modification of stairways, or modification of hardware on doors, (D) modifications of counters, (E) bathroom accessibility improvements, (F) installation, replacement, or modification of appliances to make them more accessible to individuals with a vision impairment, and installation of other assistive technologies, including remote health monitoring, (G) the addition of a bedroom or full bathroom on the main floor, (H) the installation of porch lifts or other forms of lifts, (I) the modification or installation of adaptive fire alarms, smoke detectors, and other warning systems, (J) the installation of non-slip flooring or creation of level flooring, (K) the installation of bright lighting throughout the residence or at the entry and exit of the residence, (L) the relocation or modification of laundry facilities, and (M) any other modification included in a list established and maintained in accordance with paragraph (3). (3) List of modifications The Secretary, in consultation with the Secretary of Housing and Urban Development, the Assistant Secretary for Aging of the Department of Health and Human Services, and the Commissioner on Disabilities of the Administration for Community Living, Department of Health and Human Services, and after receiving the input of members of the public (including seniors groups and home construction, technology, health, and social services organizations), shall establish and maintain a list of any modification that, if installed on a residence of a qualified individual, would enhance the ability of such individual to remain living safely, independently, and comfortably in such residence. (e) Special rules (1) Inflation adjustment In the case of any taxable year beginning in a calendar year after 2025, each of the dollar amounts in subsections (b)(1), (b)(2)(B), and (b)(2)(C) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. Any increase determined under the preceding sentence which is not a multiple of $50 shall be rounded to the nearest multiple of $50. (2) Substantiation No credit shall be allowed under this section unless the taxpayer provides (at such time and in such manner as the Secretary may provide) such substantiation of the taxpayer\u2019s eligibility for the credit allowed under this section (and the amount thereof) as the Secretary may require. (3) Denial of double benefit To the extent that an expenditure is used for this credit in a given year, it cannot be used or applied towards another tax benefit in the same taxable year by the same taxpayer. (4) Married individuals filing separate returns In the case of any married individual who does not file a joint return for the taxable year, no credit shall be allowed under this section for such taxable year. .\n##### (b) Conforming amendments\n**(1)**\nSection 6211(b)(4)(A) of the Internal Revenue Code of 1986 is amended by inserting , 36C after 36B .\n**(2)**\nParagraph (2) of section 1324(b) of title 31, United States Code, is amended by inserting , 36C after 36B .\n**(3)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Credit for certain home accessibility improvements. .\n##### (c) Issuance of guidance by Secretary of the Treasury\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary\u2019s delegate) shall issue regulations or other guidance under subsection (d)(2)(E) of section 36C of the Internal Revenue Code of 1986 (as added by this section), which the Secretary of the Treasury (or the Secretary\u2019s delegate) shall ensure is publicly available on the internet, specifying the list of additional improvements with respect to which credit is allowable under such section. The Secretary shall biannually revise such list of additional improvements.\n##### (d) Accessibility of credit\nThe Commissioner of Internal Revenue shall make the credit allowed under section 36C of the Internal Revenue Code of 1986 (as added by this section) as accessible as possible to the public.\n##### (e) Outreach\nThe Commissioner of Internal Revenue shall conduct an outreach strategy to the public with respect to the credit allowed under section 36C of the Internal Revenue Code of 1986 (as added by this section).\n##### (f) Data sharing by the Commissioner of Social Security and Secretary of Veterans Affairs\nThe Commissioner of Social Security and the Secretary of Veterans Affairs shall each provide the Secretary of the Treasury (or the Secretary\u2019s delegate) such information and assistance as the Secretary of the Treasury (or the Secretary\u2019s delegate) may require for purposes of administering section 36C of the Internal Revenue Code of 1986 (as added by this section).\n##### (g) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n##### (h) GAO study and report\n**(1) Study**\nThe Comptroller General of the United States, in consultation with the Secretary of the Treasury, the Secretary of Housing and Urban Development, the Assistant Secretary for Aging of the Department of Health and Human Services, and the Commissioner on Disabilities of the Administration for Community Living, Department of Health and Human Services, shall conduct a study which\u2014\n**(A)**\nexamines the effectiveness of the tax credit under section 36C of the Internal Revenue Code of 1986 (as added by this Act) in terms of\u2014\n**(i)**\nthe number of residential units served (the number of units where at least 1 accessible design feature is now present);\n**(ii)**\nreductions in emergency department visits, hospitalizations, or both for qualified individuals;\n**(iii)**\nreductions in Medicare expenditures for qualified individuals;\n**(iv)**\nimprovements in activities of daily living for qualified individuals; and\n**(v)**\nreduction in symptoms of depression for qualified individuals;\n**(B)**\nprovides recommendations for ways to modify or enhance the tax credit to further assist qualified individuals who wish to live independently and safely in place, including\u2014\n**(i)**\nwhether the amount of the tax credit and the limitation based on adjusted gross income should continue to be automatically adjusted for inflation;\n**(ii)**\nwhether the tax credit should be made available to renters or landlords; and\n**(iii)**\nwhether the tax credit should be made available to builders for construction of new accessible units; and\n**(C)**\nprovides suggestions for alternative policies or changes to other existing programs that Federal and State governments could implement to\u2014\n**(i)**\nincrease the number of residential units with accessible design features; and\n**(ii)**\nassist seniors and individuals with disabilities who wish to live independently and safely in place.\nqualified individual\nsection 36C(c)\n**(2) Report**\nNot later than 3 years after the date of the enactment of this Act, the Comptroller General shall\u2014\n**(A)**\nsubmit a report to the Committees on Finance and Health, Education, Labor, and Pensions of the Senate and the Committees on Ways and Means and Energy and Commerce of the House of Representatives presenting the conclusions of the study conducted under paragraph (1) in such a manner as to inform future legislative action; and\n**(B)**\nmake such report publicly available on the Internet website of the Government Accountability Office.",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-04-07",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1315",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide a refundable credit for certain home accessibility improvements.",
      "type": "S"
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
        "updateDate": "2025-05-09T18:02:15Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2749ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to provide a refundable credit for certain home accessibility improvements.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-18T05:18:27Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to provide a refundable credit for certain home accessibility improvements.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T08:06:38Z"
    }
  ]
}
```
