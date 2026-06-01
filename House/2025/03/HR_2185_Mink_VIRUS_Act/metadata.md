# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2185?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2185
- Title: Mink VIRUS Act
- Congress: 119
- Bill type: HR
- Bill number: 2185
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2026-04-17T08:07:04Z
- Update date including text: 2026-04-17T08:07:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-18 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-18 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2185",
    "number": "2185",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "E000297",
        "district": "13",
        "firstName": "Adriano",
        "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
        "lastName": "Espaillat",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Mink VIRUS Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:04Z",
    "updateDateIncludingText": "2026-04-17T08:07:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-03-18T16:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:05:00Z",
              "name": "Referred to"
            }
          },
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-18T16:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2185ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2185\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Espaillat (for himself, Ms. Barrag\u00e1n , Mr. Frost , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo protect public health and human safety by prohibiting the farming of mink for their fur, to compensate farmers as they transition out of the industry, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mink: Vectors for Infection Risk in the United States Act or the Mink VIRUS Act .\n#### 2. Prohibition on mink farming and requirements for mink termination\n##### (a) Cessation of operations\nBeginning on the date that is 1 year after the date of enactment of this Act, no fur farm may farm mink.\n##### (b) Painless mink termination methods\nBeginning on the date that is 90 days after the date of enactment of this Act, any termination of farmed mink, whether performed in order to comply with subsection (a) or otherwise, shall be done in a manner that\u2014\n**(1)**\nmeets the definition of euthanasia specified in section 1.1 of title 9, Code of Federal Regulations (or successor regulations); and\n**(2)**\nis classified as acceptable by the most recent version of the American Veterinary Medical Association (AVMA) Guidelines for the Euthanasia of Animals made publicly available at the time the termination occurred, without regard to whether the termination is in compliance with other guidelines, including the AVMA Guidelines for the Depopulation of Animals.\n##### (c) Penalties\n**(1) Penalty for failure to cease operations**\nAny person who violates subsection (a) may be assessed a civil penalty of up to $10,000 for each day that the fur farm is not in compliance with the requirements of that subsection.\n**(2) Penalty for noncompliant termination of mink**\nAny person who violates subsection (b) may be assessed a civil penalty of up to $10,000 for each mink terminated in a manner that does not comply with the requirements of that subsection.\n##### (d) Effect on preemption\nThis section shall not be construed to preempt or limit any requirement of any law or regulation of a State or political subdivision of a State that is more restrictive than the requirements of this section.\n#### 3. Payment program\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary of Agriculture (referred to in this section as the Secretary ) shall establish and carry out a program (referred to in this section as the Program ) to provide payments to owners of fur farms whose operations involve the farming of mink.\n##### (b) Payments\nUnder the Program, the Secretary shall provide payments to fur farm owners equal to the sum of the Secretary\u2019s determination of\u2014\n**(1)**\nthe reasonable cost incurred by the owner in order to comply with sections 2(a) and 2(b); and\n**(2)**\nthe market value of the portion of the owner\u2019s fur farm, exclusive of the land, involving mink farming.\n##### (c) Market value determination\n**(1) Market value**\nThe market value referred to in subsection (b)(2) shall be calculated as the amount in cash, or on terms reasonably equivalent to cash, for which in all probability the relevant portion of the fur farm would have sold on the effective date of the valuation, after a reasonable exposure time on the competitive market, from a willing and reasonably knowledgeable seller to a willing and reasonably knowledgeable buyer, with neither acting under any compulsion to buy or sell, giving due consideration to all available economic uses of that portion of the fur farm at the time of the valuation.\n**(2) Effective date of valuation**\nIn determining the market value referred to in subsection (b)(2), the effective date of the valuation shall be the day before the date of enactment of this Act.\n##### (d) Grant condition\nAs a condition of receiving a payment under the Program, the recipient shall\u2014\n**(1)**\nnot use any payment funds for any materials, supplies, labor costs, or activities associated with operating a fur farm; and\n**(2)**\nprovide to the Secretary a permanent easement on the property on which the fur farm is located that prohibits the operation of any fur farm on the easement area.\n##### (e) Funding\nNot later than 60 days after the date of enactment of this Act, out of any funds in the Treasury not otherwise appropriated, the Secretary of the Treasury shall transfer to the Secretary of Agriculture $100,000,000 to carry out this section, to remain available until expended.\n#### 4. Definitions\nIn this Act:\n**(1) Fur**\nThe term fur means any animal skin or part of an animal skin with hair, fleece, or fur fibers attached, either in its raw or processed state. Such term\u2014\n**(A)**\ndoes not include animal skins that will be converted into leather or which in processing will have their hair, fleece, or fur fiber completely removed; and\n**(B)**\ndoes not include cowhide with its hair attached, deerskin with its hair attached, and lambskin and sheepskin with their fleece attached.\n**(2) Fur-bearing animal**\nThe term fur-bearing animal means an animal that bears fur of marketable value.\n**(3) Fur farm**\nThe term fur farm means an operation that farms fur-bearing animals for the value of their fur, including\u2014\n**(A)**\nthe land, buildings, support facilities, and other equipment of the operation in which fur-bearing animals are, for the value of their fur, bred, slaughtered, skinned, or sold; and\n**(B)**\nthe fur-bearing animals of the operation farmed for the value of their fur and any fur produced by such fur-bearing animals that is owned by the operation.\n**(4) Mink**\nThe term mink means an American mink (Neovison vison), a European mink (Mustela lutreola), and any mink hybrid, whether alive or dead, and any parts and products from such mink or mink hybrids.\n**(5) State**\nThe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the Commonwealth of the Northern Mariana Islands, American Samoa, Guam, the United States Virgin Islands, and any other territory or possession of the United States.\n#### 5. Budgetary effects\n##### (a) Statutory PAYGO scorecards\nThe budgetary effects of this Act shall not be entered on either PAYGO scorecard maintained pursuant to section 4(d) of the Statutory Pay-As-You-Go Act of 2010 ( Public Law 111\u2013139 ; 2 U.S.C. 933(d) ).\n##### (b) Senate PAYGO scorecards\nThe budgetary effects of this Act shall not be entered on any PAYGO scorecard maintained for the purposes of section 4106 of H. Con. Res. 71 (115th Congress).",
      "versionDate": "2025-03-18",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-14T12:25:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-18",
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
          "measure-id": "id119hr2185",
          "measure-number": "2185",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-18",
          "originChamber": "HOUSE",
          "update-date": "2025-06-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2185v00",
            "update-date": "2025-06-13"
          },
          "action-date": "2025-03-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Mink: Vectors for Infection Risk in the United States Act or the Mink VIRUS Act</strong></p><p>This bill prohibits the farming of mink for their fur beginning one year after the bill's enactment and establishes a compensation program.</p><p>Beginning 90 days after the bill's enactment, any termination of farmed mink must be done in a manner that (1) meets the definition of<em> euthanasia</em> specified in Department of Agriculture (USDA) regulations\u00a0(i.e., the humane destruction of an animal accomplished by a method that produces rapid unconsciousness and subsequent death without evidence of pain or distress, or that utilizes anesthesia that causes painless loss of consciousness and subsequent death); and (2) is classified as acceptable by the American Veterinary Medical Association Guidelines for the Euthanasia of Animals.</p><p>This prohibition and these requirements do not preempt or limit any state law or regulation that is more restrictive. Further, any person in violation of this prohibition or these requirements is subject to civil penalties.</p><p>USDA must establish a payment program to compensate fur farm owners whose operations involve the farming of mink. Under the program, USDA must provide payments\u00a0for (1) the reasonable costs incurred to comply with this bill, and (2) the market value of the portion of the\u00a0farm involving mink farming (exclusive of the land). Fur farm owners may not use payment funds for fur farm operations. Further, the owner must provide USDA with a permanent property easement that prohibits the operation of any fur farm on the easement area.</p>"
        },
        "title": "Mink VIRUS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2185.xml",
    "summary": {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mink: Vectors for Infection Risk in the United States Act or the Mink VIRUS Act</strong></p><p>This bill prohibits the farming of mink for their fur beginning one year after the bill's enactment and establishes a compensation program.</p><p>Beginning 90 days after the bill's enactment, any termination of farmed mink must be done in a manner that (1) meets the definition of<em> euthanasia</em> specified in Department of Agriculture (USDA) regulations\u00a0(i.e., the humane destruction of an animal accomplished by a method that produces rapid unconsciousness and subsequent death without evidence of pain or distress, or that utilizes anesthesia that causes painless loss of consciousness and subsequent death); and (2) is classified as acceptable by the American Veterinary Medical Association Guidelines for the Euthanasia of Animals.</p><p>This prohibition and these requirements do not preempt or limit any state law or regulation that is more restrictive. Further, any person in violation of this prohibition or these requirements is subject to civil penalties.</p><p>USDA must establish a payment program to compensate fur farm owners whose operations involve the farming of mink. Under the program, USDA must provide payments\u00a0for (1) the reasonable costs incurred to comply with this bill, and (2) the market value of the portion of the\u00a0farm involving mink farming (exclusive of the land). Fur farm owners may not use payment funds for fur farm operations. Further, the owner must provide USDA with a permanent property easement that prohibits the operation of any fur farm on the easement area.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr2185"
    },
    "title": "Mink VIRUS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mink: Vectors for Infection Risk in the United States Act or the Mink VIRUS Act</strong></p><p>This bill prohibits the farming of mink for their fur beginning one year after the bill's enactment and establishes a compensation program.</p><p>Beginning 90 days after the bill's enactment, any termination of farmed mink must be done in a manner that (1) meets the definition of<em> euthanasia</em> specified in Department of Agriculture (USDA) regulations\u00a0(i.e., the humane destruction of an animal accomplished by a method that produces rapid unconsciousness and subsequent death without evidence of pain or distress, or that utilizes anesthesia that causes painless loss of consciousness and subsequent death); and (2) is classified as acceptable by the American Veterinary Medical Association Guidelines for the Euthanasia of Animals.</p><p>This prohibition and these requirements do not preempt or limit any state law or regulation that is more restrictive. Further, any person in violation of this prohibition or these requirements is subject to civil penalties.</p><p>USDA must establish a payment program to compensate fur farm owners whose operations involve the farming of mink. Under the program, USDA must provide payments\u00a0for (1) the reasonable costs incurred to comply with this bill, and (2) the market value of the portion of the\u00a0farm involving mink farming (exclusive of the land). Fur farm owners may not use payment funds for fur farm operations. Further, the owner must provide USDA with a permanent property easement that prohibits the operation of any fur farm on the easement area.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr2185"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2185ih.xml"
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
      "title": "Mink VIRUS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mink VIRUS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mink: Vectors for Infection Risk in the United States Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect public health and human safety by prohibiting the farming of mink for their fur, to compensate farmers as they transition out of the industry, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:34Z"
    }
  ]
}
```
