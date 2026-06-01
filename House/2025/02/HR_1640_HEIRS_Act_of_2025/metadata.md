# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1640?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1640
- Title: HEIRS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1640
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-01-31T03:36:14Z
- Update date including text: 2026-01-31T03:36:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1640",
    "number": "1640",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "HEIRS Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-31T03:36:14Z",
    "updateDateIncludingText": "2026-01-31T03:36:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:06:10Z",
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
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MO"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MD"
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
      "sponsorshipDate": "2025-02-26",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1640ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1640\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Ms. Williams of Georgia (for herself, Mrs. Fletcher , Mr. Cleaver , Mr. Donalds , Mr. Bishop , Mr. Mfume , Ms. Norton , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo establish a grant program for States that adopt the Uniform Partition of Heirs Property Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Heirs Estate Inheritance Resolution and Succession Act of 2025 or the HEIRS Act of 2025 .\n#### 2. Grants for eligible entities that adopt the Uniform Partition of Heirs Property Act\n##### (a) In general\nThe Secretary of Housing and Urban Development shall, not later than 1 year after the date of the enactment of this section, establish a grant program that provides amounts to eligible entities that\u2014\n**(1)**\nbefore the date of the enactment of this section, had enacted or adopted the Uniform Partition of Heirs Property Act as approved and recommended for enactment in all the States by the National Conference of Commissioners on Uniform State Laws in 2010 or a similar law that the Secretary determines is a substantial equivalent; and\n**(2)**\non or after the date of the enactment of this section, enact or adopt the Uniform Partition of Heirs Property Act as approved and recommended for enactment in all the States by the National Conference of Commissioners on Uniform State Laws in 2010 or a similar law that the Secretary determines is a substantial equivalent.\n##### (b) Use of amounts\n**(1) In general**\nEach eligible entity that receives amounts under this section shall use such amounts to assist residents of such eligible entity with bona fide expenses relating to establishing and documenting property ownership rights or settling a decedent\u2019s estate, including fees and costs related to obtaining title reports and title abstracts, copies of public records, land surveys, estate planning, heirs search or tracing services, recording and filing fees, notary fees, and legal fees and expenses.\n**(2) Layering of assistance**\nAn eligible entity that receives amounts under this section may use such amounts to assist residents of such State who are receiving assistance from other sources, including Federal, State, local, private, public, and nonprofit sources.\n##### (c) Regulations and criteria for selection\nThe Secretary shall, not later than 1 year after the date of the enactment of this section, issue a rule to carry out this section, that includes criteria for the selection of recipients.\n##### (d) Authorization of appropriations\n**(1) In general**\nThere are authorized to be appropriated to the Secretary of Housing and Urban Development $30,000,000 each of year fiscal years 2026 through 2036 to carry out this section.\n**(2) Availability**\nAny amounts appropriated under this subsection shall remain available until expended.\n##### (e) Definitions\nIn this section:\n**(1) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(2) Eligible entity**\nThe term eligible entity means a State and a unit of general local government as such terms are defined in section 102 of title 1 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302 ) a territory, or a Tribal government.\n#### 3. Grants to provide assistance relating to heirs\u2019 property resolution\n##### (a) In general\nThe Secretary of Housing and Urban Development shall carry out a program under this section to provide grants each year to eligible entities to use to provide housing counseling, legal assistance, and financial assistance related to title clearing and home retention efforts for owners of heirs\u2019 property.\n##### (b) Awards\nThe Secretary shall consider the following when awarding grants under this section:\n**(1)**\nWhether the eligible entity has a proven track record of\u2014\n**(A)**\nproviding assistance to homeowners;\n**(B)**\ntargeting services to minority and low- and moderate-income persons; and\n**(C)**\nproviding services in neighborhoods that have a high concentrations of minority persons or low- and moderate-income persons.\n**(2)**\nWhether the eligible entity has planned or existing partnerships with other eligible entities.\n**(3)**\nWhether the eligible entity is located in an area with a high number of owners of heirs\u2019 property, as determined by the Secretary.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary, for grants under this section, $10,000,000 in each of fiscal years 2026 through 2030.\n##### (d) Definitions\nFor purposes of this section, the following definitions shall apply:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na HUD approved housing counseling agency;\n**(B)**\na legal services clinics operated by an institute of higher education; or\n**(C)**\na qualifiying nonprofit.\n**(2) Heirs\u2019 property**\nThe term heirs\u2019 property means residential property for which title passed by operation of law through intestacy and is held by two or more heirs as tenants in common.\n**(3) Hud approved housing counseling agency**\nThe term HUD approved housing counseling agency means a housing counseling agency found eligible to receive assistance by the Department of Housing and Urban Development under section 106(a)(2) of the Housing and Urban Development Act of 1968.\n**(4) Low- and moderate-income persons**\n**(A) In general**\nThe term low- and moderate-income persons means a person whose household income does not exceed 120 percent of the median income for the area, as determined by the Secretary, within which\u2014\n**(i)**\nthe heirs\u2019 property which respect to which the homeowner is seeking assistance is located; or\n**(ii)**\nthe place of residence of the homeowner is located.\n**(B) Exception**\nIf the area described in subparagraph (A) is a high-cost area, as determined by the Secretary, the term low- and moderate-income persons means a homeowner whose household income does not exceed 140 percent of the median income for the area.\n**(5) Qualifying nonprofit**\nThe term qualifying nonprofit means a nonprofit, mission-driven entity that, as determined by the Secretary\u2014\n**(A)**\nhas a track record of providing assistance to homeowners;\n**(B)**\ntargets services to minority and low- and moderate-income persons; or\n**(C)**\nprovides services in neighborhoods that have high concentrations of minority persons and low- and moderate-income persons.\n**(6) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n#### 4. Heirs\u2019 property housing counseling\nSection 106(g) of the Housing and Urban Development Act of 1968 ( 12 U.S.C. 1701x(g) ) is amended by adding at the end the following new paragraph:\n(6) Counseling with respect to heirs\u2019 property (A) In general Any nonprofit organization that receives amounts under this section shall, when providing homeownership counseling services to consumers\u2014 (i) explain to such consumer what heirs\u2019 property is, the risks associated with heirs\u2019 property, and how to avoid heirs\u2019 property issues; and (ii) inform consumers of all available estate planning and title clearing options, assistance, and services, including those offered under sections 2 and 3 of the Heirs Estate Inheritance Resolution and Succession Act of 2025 . (B) Referral The Secretary shall ensure that each nonprofit organization that receives amounts under this section knows how to refer consumers, where appropriate, to mission-driven nonprofit organizations and legal services clinics operated by institutes of higher education that are capable of assisting a consumer to clear title and with general estate planning. (C) Heirs\u2019 property The term heirs\u2019 property means residential property for which title passed by operation of law through intestacy and is held by two or more heirs as tenants in common. .",
      "versionDate": "2025-02-26",
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
            "updateDate": "2025-07-24T13:58:31Z"
          },
          {
            "name": "Housing finance and home ownership",
            "updateDate": "2025-07-24T13:58:36Z"
          },
          {
            "name": "Low- and moderate-income housing",
            "updateDate": "2025-07-24T13:58:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-03-21T15:14:57Z"
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
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1640ih.xml"
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
      "title": "HEIRS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:53Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEIRS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Heirs Estate Inheritance Resolution and Succession Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program for States that adopt the Uniform Partition of Heirs Property Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:29Z"
    }
  ]
}
```
