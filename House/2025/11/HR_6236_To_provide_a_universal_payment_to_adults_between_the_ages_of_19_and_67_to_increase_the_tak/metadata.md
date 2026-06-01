# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6236?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6236
- Title: BOOST Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6236
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-01-13T15:59:46Z
- Update date including text: 2026-01-13T15:59:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6236",
    "number": "6236",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000481",
        "district": "12",
        "firstName": "Rashida",
        "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
        "lastName": "Tlaib",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "BOOST Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-13T15:59:46Z",
    "updateDateIncludingText": "2026-01-13T15:59:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:03:10Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "DC"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "LA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-11-28",
      "state": "MD"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6236ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6236\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Tlaib (for herself, Ms. Norton , Ms. Lee of Pennsylvania , Mrs. McIver , Ms. Omar , Mr. Thanedar , Mr. Carter of Louisiana , Mrs. Watson Coleman , and Ms. Pressley ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide a universal payment to adults between the ages of 19 and 67 to increase the take-home pay of American workers and enhance their financial stability, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Building Our Opportunities to Survive and Thrive Act of 2025 or the BOOST Act of 2025 .\n#### 2. Establishment of a universal adult assistance program\n##### (a) Definitions\nIn this section:\n**(1) Commissioner**\nThe term Commissioner means the Commissioner of Social Security.\n**(2) Deputy commissioner**\nThe term Deputy Commissioner means the Deputy Commissioner of the Office of Universal Adult Assistance.\n**(3) Qualifying adult**\nThe term qualifying adult means, with respect to a month, an individual who\u2014\n**(A)**\nresides in the United States;\n**(B)**\nis\u2014\n**(i)**\na citizen or national of the United States; or\n**(ii)**\na qualified alien (as defined in section 431 of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1641 )); and\n**(C)**\nis at least 19 years old on the last day of such month and less than 68 years old on the last day of such month.\n##### (b) Establishment of the office of universal adult assistance\n**(1) In general**\nThere is established within the Social Security Administration an office to be known as the Office of Universal Adult Assistance. The Office shall be headed by a Deputy Commissioner who shall be appointed by the Commissioner of Social Security.\n**(2) Responsibilities of deputy commissioner**\nThe Commissioner, acting through the Deputy Commissioner, shall\u2014\n**(A)**\nhire such personnel as are necessary for the Office of Universal Adult Assistance and make employment decisions with regard to such personnel;\n**(B)**\nhave authority to enter into such contracts or cooperative agreements with other agencies and departments as are necessary to ensure the efficiency of the program;\n**(C)**\nmake adult assistance payments to qualified adults in accordance with this section;\n**(D)**\ndetermine eligibility for adult assistance payments under subsection (c);\n**(E)**\nestablish and maintain a system of records relating to the administration of this section;\n**(F)**\nprevent fraud and abuse relating to adult assistance payments;\n**(G)**\nprovide information to the public in relation to adult assistance payments, including eligibility requirements, the application process, payment amounts, and limitations on payments;\n**(H)**\ntailor culturally and linguistically competent education and outreach toward increasing utilization rates of adult assistance payments;\n**(I)**\nissue an annual report to Congress detailing the effect of adult assistance payments, including\u2014\n**(i)**\nthe number of individuals receiving payments;\n**(ii)**\nthe total amount of funds disbursed;\n**(iii)**\ndemographic data of individuals receiving payments; and\n**(iv)**\nsuch other information as the Deputy Commissioner determines is necessary; and\n**(J)**\nissue such regulations as may be necessary to carry out the purposes of this section.\n**(3) Availability of data**\nThe Commissioner shall make available to the Deputy Commissioner such data as the Commissioner determines necessary to enable the Deputy Commissioner to effectively carry out the responsibilities described in paragraph (2).\n##### (c) Adult assistance payments\n**(1) In general**\nFor every month after December 31, 2025, the Commissioner shall pay to each qualified adult who has in effect an application approved under subsection (e) an adult assistance payment of $250.\n**(2) Penalties**\nSection 208 of the Social Security Act ( 42 U.S.C. 408 ) shall apply with respect to adult assistance payments under this section in the same manner as such section 208 applies with respect to monthly insurance benefits under title II of such Act.\n##### (d) Inflation adjustment\n**(1) In general**\nIn the case of any calendar year beginning after 2026, the $250 amount in paragraph (1) of subsection (c) shall be increased by an amount equal to\u2014\n**(A)**\nsuch dollar amount, multiplied by\n**(B)**\nthe cost-of-living adjustment determined under section 1(f)(3) of the Internal Revenue Code of 1986 for the calendar year, determined by substituting 2026 for 2016 in subparagraph (A)(ii) thereof.\n**(2) Rounding**\nIf any increase determined under paragraph (1) is not a multiple of $1, such increase shall be rounded to the next lowest multiple of $1.\n##### (e) Application\n**(1) In general**\nNo adult assistance payment shall be made to an individual unless the Commissioner has approved an application for such payment in accordance with the requirements of this paragraph.\n**(2) Application requirements**\nAn individual applying for an adult assistance payment as a qualifying adult under this section shall provide the Commissioner with an application in such form and manner as the Commissioner shall require, and such application shall include\u2014\n**(A)**\nthe name, date of birth, and social security number or taxpayer identification number of the qualifying adult; and\n**(B)**\nsuch other information as the Commissioner deems necessary.\n##### (f) Income disregard\nAn adult assistance payment made under this section shall not be taken into account\u2014\n**(1)**\nas income for purposes of the Internal Revenue Code of 1986, or\n**(2)**\nas income or resources for purposes of determining the eligibility of any individual for benefits or assistance, or the amount or extent of benefits or assistance, under any Federal program or under any State or local program financed in whole or in part with Federal funds.\n#### 3. Establishment of a tax on adjusted gross income\n##### (a) In general\nSubtitle A of the Internal Revenue Code of 1986 is amended by inserting after chapter 2A the following new chapter:\n2B Supplemental Individual Income Tax 1421. Supplemental tax on adjusted gross income (a) Imposition of tax In addition to the tax imposed by section 1, there is hereby imposed for each taxable year on the adjusted gross income (as defined in section 62) of every individual (other than an estate or trust) a tax equal to 2.5 percent of so much of the adjusted gross income of such individual as exceeds the exemption amount determined under subsection (b). (b) Exemption amount For purposes of this section, the term exemption amount means\u2014 (1) in the case of a joint return, $60,000, and (2) in any other case, one-half of the amount in paragraph (1). (c) Inflation adjustment (1) In general In the case of any taxable year beginning after 2026, the $60,000 amount in paragraph (1) of subsection (b) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting 2026 for 2016 in subparagraph (A)(ii) thereof. (2) Rounding If any increase determined under paragraph (1) is not a multiple of $100, such increase shall be rounded to the next lowest multiple of $100. (d) No offsetting credits or deductions (1) General rule After adjusted gross income (within the meaning of section 62) has been determined and reduced by the exemption amount in subsection (b), no other credit, deduction, exclusion, refund, rebate, or similar tax benefit may be applied to reduce the tax imposed by this section. (2) Prohibition on carryovers No unused amount of any credit or deduction disallowed under paragraph (1) may be carried forward or back to any other taxable year for purposes of offsetting the tax imposed by this section. (e) Regulations The Secretary shall prescribe such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section, including rules for the withholding and estimated tax requirements attributable to the tax imposed by this section. .\n##### (b) Clerical amendment\nThe table of chapters for subtitle A of the Internal Revenue Code of 1986 is amended by inserting after the item relating to chapter 2A the following new item:\nChapter 2B. Supplemental individual income tax. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-11-20",
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
        "updateDate": "2026-01-13T15:59:46Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6236ih.xml"
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
      "title": "BOOST Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BOOST Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Building Our Opportunities to Survive and Thrive Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide a universal payment to adults between the ages of 19 and 67 to increase the take-home pay of American workers and enhance their financial stability, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T05:48:24Z"
    }
  ]
}
```
