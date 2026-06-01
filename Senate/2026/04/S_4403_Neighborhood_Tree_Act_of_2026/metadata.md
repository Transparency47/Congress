# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4403?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4403
- Title: Neighborhood Tree Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4403
- Origin chamber: Senate
- Introduced date: 2026-04-27
- Update date: 2026-05-11T20:28:26Z
- Update date including text: 2026-05-11T20:28:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in Senate
- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-04-27: Introduced in Senate

## Actions

- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4403",
    "number": "4403",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Neighborhood Tree Act of 2026",
    "type": "S",
    "updateDate": "2026-05-11T20:28:26Z",
    "updateDateIncludingText": "2026-05-11T20:28:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T22:57:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4403is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4403\nIN THE SENATE OF THE UNITED STATES\nApril 27, 2026 Mr. Booker (for himself, Mrs. Gillibrand , Mr. Kim , Ms. Duckworth , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Cooperative Forestry Assistance Act of 1978 to provide States and communities with additional assistance to plant and maintain trees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Neighborhood Tree Act of 2026 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe presence of a healthy and well-maintained urban forest can\u2014\n**(A)**\nsupport\u2014\n**(i)**\nthe physical and mental health of community residents;\n**(ii)**\nthe regulation of air quality;\n**(iii)**\nthe mitigation of the urban heat island effect;\n**(iv)**\nthe reduction of energy demand; and\n**(v)**\nstormwater management; and\n**(B)**\nprovide other benefits;\n**(2)**\naccording to research of the Forest Service, the estimated value of benefits described in paragraph (1) exceeds $18,000,000,000;\n**(3)**\nthe maintenance and management of an urban forest offers additional opportunities relating to workforce development, job creation, and enhancement of property values;\n**(4)**\nurban forest canopy cover is inequitably distributed among racial groups and income levels, exacerbating disparities in exposure, for example, to the urban heat island effect and in related health risks or financial burdens relating to cooling;\n**(5)**\nthe effects of historical discriminatory policies, such as redlining, continue to have effects on urban environments;\n**(6)**\na recent analysis shows that\u2014\n**(A)**\nurbanized neighborhoods with mostly people of color have 33 percent less tree canopy on average than majority white neighborhoods; and\n**(B)**\nlow-income neighborhoods have 41 percent less tree cover than neighborhoods with low rates of poverty;\n**(7)**\nadditional analyses of cities in the United States found that\u2014\n**(A)**\ncommunities primarily inhabited by United States-born, white populations contain more than twice the urban forest canopy cover of communities primarily inhabited by racial and ethnic minorities; and\n**(B)**\nthere were elevated land temperatures in formerly redlined areas compared to their nonredlined counterparts, by an average 2.6 degrees Celsius and up to 7 degrees Celsius; and\n**(8)**\nto reduce disparities in the enjoyment of the social, environmental, and economic benefits of healthy and well-maintained urban forests and manage risks relating to heat exposure and other urban stressors, the Federal Government should accelerate actions to enhance the health and resilience of urban forests, with investment in priority communities.\n#### 3. Neighborhood Tree Fund\nSection 9 of the Cooperative Forestry Assistance Act of 1978 ( 16 U.S.C. 2105 ) is amended\u2014\n**(1)**\nby redesignating subsections (h) and (i) as subsections (i) and (j), respectively; and\n**(2)**\nby inserting after subsection (g) the following:\n(h) Neighborhood Tree Fund (1) In general Consistent with the purposes described in subsection (b), the Secretary shall establish the Neighborhood Tree Fund (referred to in this subsection as the Fund ). (2) Assistance The Secretary shall use amounts from the Fund to provide assistance to eligible entities described in paragraph (3) to increase and improve the overall health of the tree canopy in a community. (3) Eligibility An entity that is eligible to receive assistance under paragraph (2) is\u2014 (A) a State; (B) an Indian Tribe; and (C) a local unit of government, approved organization, or local community tree volunteer group described in subsection (b)(4). (4) Requirements The Secretary, in consultation with the Secretary of Housing and Urban Development, shall establish requirements for the receipt of assistance under paragraph (2), including requirements with respect to\u2014 (A) engagement with communities and stakeholders; (B) the conduct of a tree canopy assessment; (C) the use of climate change science in the design of a project using the assistance; (D) the conduct of site preparation and tree species selection; and (E) the conduct of monitoring and maintenance to ensure the successful establishment of the tree canopy. (5) Priority The Secretary shall give priority to the provision of assistance under paragraph (2) to eligible entities that propose projects that\u2014 (A) include and prioritize tree planting and tree maintenance in\u2014 (i) a census tract with a poverty rate of not less than 20 percent, as measured by the 5-year data series available from the American Community Survey of the Bureau of the Census for the period of 2014 through 2018, including such a census tract that includes an area that was designated as hazardous or definitely declining in maps drawn by the Home Owners\u2019 Loan Corporation; or (ii) a community or neighborhood with lower tree canopy and higher maximum daytime summer temperatures compared to surrounding communities or neighborhoods, as determined by the Secretary, based on publicly available information; (B) optimize outcomes for climate mitigation and resilience for the purpose of public health, as determined by the Secretary; or (C) advance community-led urban agroforestry or tree-based local food production to increase green infrastructure, reduce urban heat, and improve environmental and public health outcomes. (6) Limitations on use of amounts for community tree assessments Not more than 10 percent of the amount made available under paragraph (7) for a fiscal year may be used for the development of community tree assessments. (7) Authorization of appropriations There are authorized to be appropriated for deposit into the Fund, for use by the Secretary to carry out this subsection, not less than\u2014 (A) $100,000,000 for fiscal year 2027; (B) $200,000,000 for fiscal year 2028; (C) $400,000,000 for fiscal year 2029; (D) $600,000,000 for fiscal year 2030; and (E) $700,000,000 for fiscal year 2031. .\n#### 4. National Urban and Community Forestry Advisory Council composition\nSection 9(g)(2)(A) of the Cooperative Forestry Assistance Act of 1978 ( 16 U.S.C. 2105(g)(2)(A) ) is amended\u2014\n**(1)**\nin the matter preceding clause (i), by striking 15 and inserting 16 ;\n**(2)**\nin each of clauses (i) through (viii), by striking the comma at the end and inserting a period;\n**(3)**\nin clause (ix), by striking , and at the end and inserting a period; and\n**(4)**\nby striking clause (x) and inserting the following:\n(x) 3 members who are not officers or employees of any governmental body and who have expertise and have been active in urban and community forestry, of whom\u2014 (I) 1 is a resident of a community with a population of less than 50,000 as of the most recent census; and (II) 1 is a resident of a low-income community, as determined by the Secretary. .",
      "versionDate": "2026-04-27",
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
        "actionDate": "2026-04-23",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "8474",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Neighborhood Tree Act of 2026",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-05-11T20:28:25Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4403is.xml"
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
      "title": "Neighborhood Tree Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-06T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Neighborhood Tree Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Cooperative Forestry Assistance Act of 1978 to provide States and communities with additional assistance to plant and maintain trees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T04:18:31Z"
    }
  ]
}
```
