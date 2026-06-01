# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2064?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2064
- Title: Home of Your Own Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2064
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2025-11-05T09:05:54Z
- Update date including text: 2025-11-05T09:05:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-11 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-11 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2064",
    "number": "2064",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "L000273",
        "district": "3",
        "firstName": "Teresa",
        "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
        "lastName": "Leger Fernandez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Home of Your Own Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-05T09:05:54Z",
    "updateDateIncludingText": "2025-11-05T09:05:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-11T14:06:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "FL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "GA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "DC"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NM"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NY"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CT"
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
      "sponsorshipDate": "2025-11-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2064ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2064\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Ms. Leger Fernandez (for herself, Mr. Costa , Mr. Garc\u00eda of Illinois , Mr. Garcia of California , Ms. Lois Frankel of Florida , Mr. Johnson of Georgia , Ms. McCollum , Ms. Norton , Mrs. Ramirez , Ms. Scanlon , and Ms. Stansbury ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Housing and Urban Development to establish a program to provide homeownership assistance grants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Home of Your Own Act of 2025 .\n#### 2. Establishment of homeownership assistance grant program\n##### (a) In general\nThe Secretary of Housing and Urban Development shall, not later than 1 year after the date of the enactment of this Act, establish a homeownership assistance grant program through which amounts are provided to States and Indian tribes to assist the purchase of eligible homes by eligible persons.\n##### (b) Allocation of amounts\n**(1) In general**\nThe Secretary shall reserve 3 percent of any amounts appropriated under this Act, for a fiscal year, for grants to Indian tribes in accordance with the formula established by the Secretary pursuant to section 302 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4152 ).\n**(2) Remaining amounts**\nAfter reserving such amounts for Indian tribes under paragraph (1), the Secretary shall equitably allocate remaining amounts to participating States in accordance with a formula established by the Secretary by rule.\n##### (c) Use of amounts\n**(1) In general**\nStates and Indian tribes that receive amounts under this Act shall use such amounts to provide assistance on behalf of eligible persons for\u2014\n**(A)**\ncosts incurred acquiring an ownership interest in an eligible home by means of an eligible mortgage loan, including downpayment costs, closing costs, and costs to reduce interest rates on such loan; or\n**(B)**\npre-occupancy repairs or modifications required for a member of the household of the homebuyer to occupy the home following such acquisition, including repairs to bring the home up to inspection standards and costs associated with reasonable accommodations or reasonable modifications for a household member with a disability, when applicable.\n**(2) Amount of assistance**\nStates and Indian tribes that receive amounts under this Act may provide assistance only once on behalf of an eligible person and the amount of such assistance provided on behalf of such eligible person shall be $30,000.\n##### (d) Layering of assistance\nStates and Indian tribes that receive amounts under this Act may provide assistance on behalf of an eligible person who is receiving assistance from other sources, including other State, Federal, Indian tribe, tribal organization, private and public tax-exempt nonprofit organizations, for acquisition of an ownership interest in an eligible home.\n##### (e) Repayment of assistance if occupancy not continued\n**(1) In general**\nIf an eligible person does not continue to occupy, as a primary residence, the eligible home for which the covered person receives assistance under this Act for the 60-month period beginning when the covered person is able to lawfully occupy the eligible home, the Secretary shall require the eligible person to repay the assistance received in an amount that is proportional to the number of months the eligible person did not occupy the eligible home as a primary residence.\n**(2) Exceptions**\nThe Secretary may not require an eligible person to repay assistance under paragraph (1) if the Secretary determines that\u2014\n**(A)**\na hardship as described by the Secretary prevents the eligible person from occupying the eligible home as the primary residence; or\n**(B)**\nany amount received by the eligible person from an arm\u2019s length transaction selling the entirety of the ownership interest in the eligible home of the homebuyer to a bona fide purchaser is less than the original cost of acquisition of the home, including closing costs.\n**(3) Use of lien**\nThe State or Indian tribe that provided the assistance to the eligible person may place a lien on the eligible home for the purpose of recapturing such assistance.\n**(4) Use of recaptured amounts**\nAny assistance repaid pursuant to paragraph (1) shall be used to provide assistance to other covered persons.\n##### (f) Assistance amounts excluded from federal taxation\nFor purposes of the Internal Revenue Code of 1986, gross income shall not include any assistance provided under this Act.\n##### (g) Rule of construction\nAssistance provided to an eligible person by a State or Indian tribe under this section may not be considered funds from a prohibited source for the purposes of section 203(b)(9)(C) of the National Housing Act ( 12 U.S.C. 1709(b)(9)(C) ).\n#### 3. Administration of grants by states and indian tribes\n##### (a) Administration by states\n**(1) In general**\nThe Secretary shall require that each State receiving grant amounts under this Act\u2014\n**(A)**\nsubmit an annual plan to the Secretary with respect to implementing and complying with the requirements of this Act; and\n**(B)**\ndistribute not less than 25 percent of the amounts allocated to the State through community development financial institutions.\n**(2) Annual plan**\nThe annual plan required under paragraph (1) may be included in the Annual Action Plan submitted to the Secretary by such State.\n**(3) Outsourcing permitted**\nThe Secretary may permit a State to contract with one or more of the following to provide amounts to eligible persons on behalf of the State:\n**(A)**\nA tax-exempt private or public nonprofit organization approved by the Secretary.\n**(B)**\nA community development financial institution.\n##### (b) Administration by indian tribes\n**(1) In general**\nThe Secretary shall require that each Indian tribe receiving grant amounts under this Act\u2014\n**(A)**\nsubmit an annual plan to the Secretary with respect to implementing and complying with the requirements of this Act; and\n**(B)**\nconsider distributing some or all amounts allocated to the Indian tribe through community development financial institutions.\n**(2) Annual plan**\nThe annual plan required under paragraph (1) may be included in the Indian Housing Plan submitted to the Secretary by such Indian tribe.\n**(3) Outsourcing permitted**\nThe Secretary may permit a Tribe to contract with one or more of the following to provide amounts to eligible persons on behalf of the Tribe:\n**(A)**\nA tax-exempt private or public nonprofit organization approved by the Secretary.\n**(B)**\nA Tribally designated housing entity.\n**(C)**\nAn intertribal consortium.\n**(D)**\nA community development financial institution.\n**(4) Preference permitted**\nAn Indian tribe that receives amounts under this Act may provide preference to eligible persons who are members of such Indian tribe as well as to members of other Indian tribes.\n#### 4. Financial counseling requirement\n##### (a) In general\nA State or Indian tribe may only provide assistance under this Act to an eligible person if such eligible person, before receiving such assistance, completes a financial counseling program with respect to the responsibilities and financial management of homeownership.\n##### (b) Approval and manner of program\nThe financial counseling program shall be conducted by an entity that provides financial counseling approved by, and in a manner acceptable to\u2014\n**(1)**\nthe Secretary; or\n**(2)**\nthe Indian tribe or State providing assistance to the eligible person.\n#### 5. Authorization of appropriations; administrative costs\n##### (a) In general\nThere is authorized to be appropriated $6,700,000,000 for each of fiscal years 2026 through 2030 to carry out this Act.\n##### (b) Program administration\n**(1) For states**\nNot more than 7 percent of any amounts provided to a State under this Act may be used by such State to cover administrative costs.\n**(2) For indian tribes**\nNot more than 10 percent of any amounts provided to an Indian Tribe under this Act may be used by such Indian Tribe to cover administrative costs.\n##### (c) Training and technical assistance\nNot more than 3 percent of any amounts appropriated under this Act may be used by the Secretary to provide training and technical assistance to States and Indian tribes.\n#### 6. Definitions\nIn this Act:\n**(1) Community development financial institution**\nThe term community development financial institution has the meaning given the term in section 103 of the Community Development Banking and Financial Institutions Act of 1994.\n**(2) Eligible home**\nThe term eligible home means a residential property, including a condominium, cooperative, or manufactured housing unit, that\u2014\n**(A)**\nconsists of 1 to 4 dwelling units, including accessory dwelling units;\n**(B)**\nis subject to a mortgage, and\u2014\n**(i)**\nmeets the underwriting requirements and dollar amount limitations for acquisition by the Federal National Mortgage Association or the Federal Home Loan Mortgage Corporation;\n**(ii)**\nis made, insured, or guaranteed under any program administered by the Secretary;\n**(iii)**\nis made, insured, or guaranteed by the Rural Housing Administrator of the Department of Agriculture;\n**(iv)**\nis a qualified mortgage, as defined in section 129C(b)(2) of the Truth in Lending Act ( 15 U.S.C. 1639c(b)(2) );\n**(v)**\nis made, insured, or guaranteed by the Secretary of Veterans Affairs pursuant to chapter 37 of title 38, United States Code; or\n**(vi)**\nin the case of a residential property located on tribal trust or reservation land, meets such requirements as the Secretary determines appropriate for consumer protection; and\n**(C)**\nshall be occupied by an eligible person as a primary residence.\n**(3) Eligible person**\n**(A) In general**\nThe term eligible person means\u2014\n**(i)**\na person who, as self-attested by the person, is a first-time homebuyer ; and\n**(ii)**\nis a part of a household, the income of which does not exceed\u2014\n**(I)**\nin the case of a person purchasing an eligible home that is not located on Indian tribe land, 120 percent of the median income for the local area, as determined by the Secretary, within which\u2014\n**(aa)**\nthe eligible home, for which the ownership interest is to be acquired using such assistance, is located; or\n**(bb)**\nthe place of residence of the homebuyer is located; and\n**(II)**\nin the case of a person who is purchasing an eligible home that is located on Indian tribe land, the greater of 120 percent of the median income of the United States or 120 percent of the median income for the local area, as determined by the Secretary, within which\u2014\n**(aa)**\nthe eligible home, for which the ownership interest is to be acquired using such assistance, is located; or\n**(bb)**\nthe place of residence of the homebuyer is located.\n**(B) Exception**\nIf the Secretary determines that the area described in subparagraph (A)(ii) is a high cost-of-living area, then the eligible person is required to be a part of a household, the income of which does not exceed 150 percent of the median income for the area, as determined by the Secretary.\n**(4) First-time homebuyer**\nThe term first-time homebuyer has the meaning given the term is defined in section 104 of the Cranston Gonzalez National Affordable Housing Act ( 42 U.S.C. 12704 ).\n**(5) Indian tribe**\nThe term Indian tribe has the meaning given the term in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ).\n**(6) Ownership interest**\nThe term ownership interest means any ownership, excluding any interest in heir property, in\u2014\n**(A)**\nreal estate in fee simple;\n**(B)**\na leasehold on real estate, under a lease that is not less than 10 years longer than the term of the mortgage;\n**(C)**\na fee interest in, or long-term leasehold interest in, real estate consisting of a one-family unit in a multifamily project, including a project in which the dwelling units are attached, or are manufactured housing units, semi-detached, or detached, and an undivided interest in the common areas and facilities which serve the project.\n**(7) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(8) State**\nThe term State means the 50 States of the United States, the District of Columbia, the Commonwealth of Puerto Rico, Guam, the Commonwealth of the Northern Mariana Islands, the Virgin Islands, and American Samoa.",
      "versionDate": "2025-03-11",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Housing and community development funding",
            "updateDate": "2025-07-24T14:17:38Z"
          },
          {
            "name": "Housing finance and home ownership",
            "updateDate": "2025-07-24T14:17:21Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2025-07-24T14:17:45Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-07-24T14:17:56Z"
          },
          {
            "name": "Residential rehabilitation and home repair",
            "updateDate": "2025-07-24T14:17:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-05-06T19:37:35Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2064ih.xml"
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
      "title": "Home of Your Own Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Home of Your Own Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Housing and Urban Development to establish a program to provide homeownership assistance grants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:04:03Z"
    }
  ]
}
```
