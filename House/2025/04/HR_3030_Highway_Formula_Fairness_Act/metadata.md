# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3030?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3030
- Title: Highway Formula Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 3030
- Origin chamber: House
- Introduced date: 2025-04-28
- Update date: 2025-09-18T08:07:18Z
- Update date including text: 2025-09-18T08:07:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-28: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-28 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-04-28: Introduced in House

## Actions

- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-28 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3030",
    "number": "3030",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Highway Formula Fairness Act",
    "type": "HR",
    "updateDate": "2025-09-18T08:07:18Z",
    "updateDateIncludingText": "2025-09-18T08:07:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-28",
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
          "date": "2025-04-28T16:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-28T21:19:16Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3030ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3030\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2025 Mr. Stanton (for himself and Mr. Tony Gonzales of Texas ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to provide for a discretionary increase in certain highway funding to take into account population growth of a State, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Highway Formula Fairness Act .\n#### 2. Discretionary increase in certain highway funding for population growth\n##### (a) In general\nSection 104(c)(1) of title 23, United States Code, is amended\u2014\n**(1)**\nin subparagraph (B)\u2014\n**(A)**\nby striking clause (i); and\n**(B)**\nby redesignating clauses (ii) and (iii) as clauses (i) and (ii), respectively; and\n**(2)**\nby adding at the end the following:\n(C) Discretionary increase in amounts for population growth In addition to the amounts described in subparagraphs (A) and (B), the Secretary may provide an additional amount to each State that has increased in population since the previous decennial census conducted under section 141(a) of title 13, United States Code, in a proportion based on the relative increase in each such population, as determined appropriate by the Secretary . .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply beginning with the first fiscal year beginning after the date of enactment of this Act.\n#### 3. Highway formula modernization study\n##### (a) In general\nThe Secretary of Transportation, in consultation with the State departments of transportation and representatives of local governments (including metropolitan planning organizations), shall conduct a highway formula modernization study to assess the method and data used to apportion Federal-aid highway funds under subsections (b) and (c) of section 104 of title 23, United States Code, and issue recommendations relating to such method and data.\n##### (b) Assessment\nThe highway formula modernization study required under subsection (a) shall include an assessment of, based on the latest available data, whether the apportionment method described in such subsection results in\u2014\n**(1)**\nan equitable distribution of funds based on the estimated tax payments attributable to\u2014\n**(A)**\nhighway users in the State that are paid into the Highway Trust Fund; and\n**(B)**\nindividuals in the State that are paid to the Treasury, based on contributions to the Highway Trust Fund from the general fund of the Treasury; and\n**(2)**\nthe achievement of the goals described in section 101(b)(3) of title 23, United States Code.\n##### (c) Considerations\nIn the assessment under subsection (b), the Secretary shall consider the following:\n**(1)**\nThe factors described in sections 104(b), 104(f)(2), 104(h)(2), 130(f), and 144(e) of title 23, United States Code, as in effect on the date of enactment of SAFETEA\u2013LU ( Public Law 109\u201359 ; 119 Stat. 1144).\n**(2)**\nThe availability and accuracy of data necessary to calculate formula apportionments under the factors described in paragraph (1).\n**(3)**\nThe measures established under section 150 of title 23, United States Code, and whether those measures are appropriate for consideration as formula apportionment factors.\n**(4)**\nAny other factors that the Secretary determines are appropriate.\n##### (d) Recommendations\nThe Secretary, in consultation with the State departments of transportation and representatives of local governments (including metropolitan planning organizations), shall develop recommendations on a new apportionment method, including\u2014\n**(1)**\nthe factors recommended to be included in the new apportionment method;\n**(2)**\nthe weighting recommended to be applied to the factors recommended under paragraph (1); and\n**(3)**\nany other recommendations to ensure that the new apportionment method best achieves an equitable distribution of funds described under subsection (b)(1) and the goals described in subsection (b)(2).\n##### (e) Report to Congress\nNot later than 90 days after the date of enactment of this Act, the Secretary shall submit to Congress a report containing the study conducted under subsection (a) and the recommendations developed under subsection (d).",
      "versionDate": "2025-04-28",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-22T16:11:53Z"
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
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3030ih.xml"
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
      "title": "Highway Formula Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-08T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Highway Formula Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-08T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to provide for a discretionary increase in certain highway funding to take into account population growth of a State, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-08T04:33:30Z"
    }
  ]
}
```
