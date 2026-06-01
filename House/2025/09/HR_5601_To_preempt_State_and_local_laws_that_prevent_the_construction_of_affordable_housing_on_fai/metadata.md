# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5601?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5601
- Title: Faith in Housing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5601
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2025-11-18T16:56:19Z
- Update date including text: 2025-11-18T16:56:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5601",
    "number": "5601",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Faith in Housing Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-18T16:56:19Z",
    "updateDateIncludingText": "2025-11-18T16:56:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
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
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:02:20Z",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5601ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5601\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Peters (for himself and Mr. Edwards ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo preempt State and local laws that prevent the construction of affordable housing on faith lands, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Faith in Housing Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAn underproduction in housing units relative to demand has led to a housing shortage of millions of homes in the United States.\n**(2)**\nLack of housing supply and rising rent costs exacerbate inequality and reduce opportunity for many people in the United States.\n**(3)**\nPeople in the United States who are unable to afford rising housing costs can fall into homelessness, causing both personal tragedy and challenges to public and charitable social services.\n**(4)**\nHouses of worship from every major faith tradition are involved in charitable activities to support low-income people in the United States facing housing insecurity.\n**(5)**\nThe efforts of houses of worship to shelter homeless people in the United States, provide affordable or supportive housing, and serve the poor are obstructed by land use regulation that prohibits or curtails the ability of the house of worship to meet this mission.\n**(6)**\nThe ability of houses of worship to serve their mission would be enhanced by allowing them the discretion to provide for the construction of affordable homes and homeless shelters.\n**(7)**\nThe construction of housing is a form of interstate commerce that affects the economy and social welfare of the United States. State and local land use regulation has national and interstate effects on the housing shortage, level of housing insecurity and homelessness, and need for social services.\n#### 3. Preemption of State and local laws preventing affordable housing construction on faith lands\n##### (a) Definitions\nIn this section:\n**(1) Affordable housing**\nThe term affordable housing means\u2014\n**(A)**\nhousing that complies with\u2014\n**(i)**\nState or local building codes at the site of construction;\n**(ii)**\nThe International Residential Code or International Building Code of the International Code Council, as applicable to the type of structure; or\n**(iii)**\nThe Manufactured Home Construction and Safety Standards and other regulations applicable to manufactured homes adopted under the Manufactured Housing Construction and Safety Standards Act ( 42 U.S.C. 5401 et seq. );\n**(B)**\nhousing that is deed-restricted to be affordable as rental units or for homeownership to residents at a range of percentages of area median income, provided that\u2014\n**(i)**\nthe average cost among all housing units is affordable to low-income families as determined under section 3(b)(2) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(2) ); and\n**(ii)**\nall units are affordable at or below 140 percent of the area median income;\n**(C)**\nhousing that will remain affordable, according to binding commitments, for 30 years from construction or substantial rehabilitation, without regard to the term of the mortgage or to transfer of ownership;\n**(D)**\nhousing that may include preexisting or limited non-residential uses, including\u2014\n**(i)**\nground-floor facilities, such as childcare centers, operated by nonprofit community-based organizations for the provision of educational, recreational, or social services for use by the residents of the affordable housing and residents of the local community in which the housing is located; and\n**(ii)**\nany preexisting religious institutional use, if such use is limited to the preexisting total square footage;\n**(E)**\nhousing that may set aside not more than 5 percent of units for employees of the house of worship, or not more than one unit if the total number of units is at least five units, and shall otherwise comply with the Fair Housing Act ( 42 U.S.C. 3601 et seq. ) without regard to 42 U.S.C. 3607 ; and\n**(F)**\nfor affordable rental housing, housing that is managed by a nonprofit property manager with experience managing affordable housing, that has entered into an agreement for such purpose with the house of worship.\n**(2) Faith land**\nThe term faith land means real estate\u2014\n**(A)**\nowned on or before January 1, 2023, by a house of worship; or\n**(B)**\nowned for a period of not less than 5 years by a house of worship.\n**(3) House of worship**\nThe term house of worship means a church or a convention or association of churches as described in section 170(b)(1)(A)(i) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of such Code.\n**(4) Site-specific hazard**\nThe term site-specific hazard means a flood, landslide, wildfire, or similar severe disaster hazard, on the site of construction.\n##### (b) Protection of land use for affordable housing\n**(1) Authority to use faith land for affordable housing**\nThe owner of faith land shall, upon notifying in writing any applicable State or local zoning authority of its election to invoke the terms of this Act, have sole discretion to construct or substantially rehabilitate affordable housing on such land, if such affordable housing\u2014\n**(A)**\nis in or affects interstate or foreign commerce; or\n**(B)**\nis constructed using Federal assistance.\n**(2) Relation to State law**\n**(A) In general**\nAny law, regulation, or other requirement of a State or political subdivision of a State that is inconsistent with this section is preempted by the requirements under paragraph (1), but only to the extent of such inconsistency. Any provision of such law, regulation, or other requirement that is narrowly tailored to prevent site-specific hazards, and applies on equal terms to housing constructed under paragraph (1) and to all other residential construction in the jurisdiction, is not preempted.\n**(B) Inspection**\nA State or political subdivision of a State shall have the right to reasonably inspect affordable housing described in paragraph (1) to confirm that the housing conforms to the requirements described in subsection (a)(1).\n**(3) Cause of action**\nA person may assert a violation of this section as a claim or defense in a judicial proceeding and obtain injunctive or declaratory relief.\n**(4) Attorneys\u2019 fees**\nSection 722(b) of the Revised Statutes ( 42 U.S.C. 1988(b) ) is amended\u2014(1) by inserting Faith in Housing Act of 2025 , after Religious Land Use and Institutionalized Persons Act of 2000.\n**(5) Applicability**\nThis Act shall not apply to the construction or substantial rehabilitation of affordable housing on faith land unless the owner submits written notice of its intention to invoke the terms of this Act in accordance with paragraph (b)(1) of this section.",
      "versionDate": "2025-09-26",
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
        "updateDate": "2025-11-18T16:56:19Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5601ih.xml"
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
      "title": "Faith in Housing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Faith in Housing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To preempt State and local laws that prevent the construction of affordable housing on faith lands, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:15Z"
    }
  ]
}
```
