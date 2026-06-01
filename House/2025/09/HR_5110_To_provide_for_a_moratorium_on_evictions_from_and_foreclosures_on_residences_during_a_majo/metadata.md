# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5110?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5110
- Title: Federal Disaster Housing Stability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5110
- Origin chamber: House
- Introduced date: 2025-09-03
- Update date: 2025-09-18T12:24:35Z
- Update date including text: 2025-09-18T12:24:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-09-03: Introduced in House

## Actions

- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5110",
    "number": "5110",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "C001127",
        "district": "20",
        "firstName": "Sheila",
        "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
        "lastName": "Cherfilus-McCormick",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Federal Disaster Housing Stability Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-18T12:24:35Z",
    "updateDateIncludingText": "2025-09-18T12:24:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-03",
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
      "actionDate": "2025-09-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T14:01:20Z",
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
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "IN"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "MS"
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
      "sponsorshipDate": "2025-09-03",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5110ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5110\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 3, 2025 Mrs. Cherfilus-McCormick (for herself, Ms. Chu , Mr. Carson , Mr. Thompson of Mississippi , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo provide for a moratorium on evictions from and foreclosures on residences during a major disaster or emergency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Disaster Housing Stability Act of 2025 .\n#### 2. Eviction moratorium\n##### (a) Moratorium\nIn the case of any disaster, the lessor, landlord, or owner, including any individual with a legal right to pursue eviction or a possessory action, of a covered dwelling that is located within the disaster area with respect to such disaster may not, during the eviction moratorium period with respect to such area\u2014\n**(1)**\nmake, or cause to be made, any filing with the court of jurisdiction to initiate a legal action to recover possession of the covered dwelling from the tenant for nonpayment of rent or other fees or charges;\n**(2)**\ncharge fees, penalties, or other charges to the tenant related to such nonpayment of rent;\n**(3)**\nincrease the amount charged for rental of the dwelling, including by recouping such increased rent through fees or charges after the conclusion of such period;\n**(4)**\nin any manner prevent the tenant of the dwelling, if such tenant has temporarily relocated, from returning to the dwelling and re-establishing occupancy or require the tenant to be re-screened to determine any eligibility for such occupancy; or\n**(5)**\nremove or cause the removal of a tenant from a covered dwelling.\n##### (b) Notice To vacate\nIn the case of any disaster, the lessor of a covered dwelling that is located within the disaster area with respect to such disaster may not\u2014\n**(1)**\nrequire the tenant to vacate the covered dwelling before the date that is 30 days after the date on which the lessor provides the tenant with a notice to vacate; and\n**(2)**\nissue a notice to vacate under paragraph (1) until after the expiration of the eviction moratorium period with respect to such area.\n#### 3. Foreclosure moratorium\nExcept with respect to a vacant or abandoned property, in the case of any disaster, a servicer of a covered mortgage loan on a property located within the disaster area may not, during the foreclosure moratorium period with respect to such area, initiate any judicial or non-judicial foreclosure process, schedule a foreclosure sale, move for a foreclosure judgment or order of sale, or execute a foreclosure-related eviction or foreclosure sale.\n#### 4. Definitions\nFor purposes of this Act, the following definitions shall apply:\n**(1) Covered dwelling**\nThe term covered dwelling means a dwelling that is occupied by a tenant\u2014\n**(A)**\npursuant to a residential lease; or\n**(B)**\nwithout a lease or with a lease terminable under State or District of Columbia law.\n**(2) Disaster**\nThe term disaster means\u2014\n**(A)**\nany national emergency declared by the President under the National Emergencies Act ( 50 U.S.C. 1601 et seq. );\n**(B)**\nany major disaster or emergency declared by the President under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 4121 et seq. ); or\n**(C)**\nany major disaster or emergency declared by the Governor of a State, the Mayor of the District of Columbia, or the Chief Executive of an Indian Tribal government.\n**(3) Disaster area**\nThe term disaster area means, with respect to a disaster, any area that at any time is subject to the declaration of such disaster.\n**(4) Dwelling**\nThe term dwelling \u2014\n**(A)**\nhas the meaning given the term in section 802 of the Fair Housing Act ( 42 U.S.C. 3602 ); and\n**(B)**\nincludes houses and dwellings described in section 803(b) of such Act ( 42 U.S.C. 3603(b) ).\n**(5) Eviction moratorium period**\nThe term eviction moratorium period means, with respect to a disaster area, the 120-day period that begins upon the declaration by the President of the disaster that such area is subject to.\n**(6) Covered mortgage loan**\nThe term covered mortgage loan includes any consumer credit transaction (within the meaning of such term as used in the Truth in Lending Act ( 15 U.S.C. 1601 et seq. )), other than temporary financing such as a construction loan, that is secured by a mortgage, deed of trust, or other consensual security interest on a 1- to 4-unit dwelling or on residential real property that includes a 1- to 4-unit dwelling including individual units of condominiums and cooperatives that is secured by a first or subordinate lien on residential real property (including individual units of condominiums and cooperatives) designed principally for the occupancy of from 1 to 4 families, including any such secured loan the proceeds of which are used to prepay or pay off an existing loan secured by the same property, but such term does not include a credit transaction under an open-end credit plan other than a reverse mortgage.\n**(7) Foreclosure moratorium period**\nThe term foreclosure moratorium period means, with respect to a disaster area, the 6-month period that begins upon the declaration of the disaster for which such declaration was made.\n#### 5. Applicability\nThis Act shall apply with respect to any disaster for which the declaration of the disaster is in effect on the date of the enactment of this Act and any disaster for which such declaration is made after such date of enactment.",
      "versionDate": "2025-09-03",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-18T12:24:35Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5110ih.xml"
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
      "title": "Federal Disaster Housing Stability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-06T07:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Disaster Housing Stability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-06T07:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for a moratorium on evictions from and foreclosures on residences during a major disaster or emergency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-06T07:33:31Z"
    }
  ]
}
```
