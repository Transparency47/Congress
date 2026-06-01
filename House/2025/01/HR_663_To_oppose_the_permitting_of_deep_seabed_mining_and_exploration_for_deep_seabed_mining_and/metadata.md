# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/663?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/663
- Title: To oppose the permitting of deep seabed mining and exploration for deep seabed mining, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 663
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-03-26T08:06:48Z
- Update date including text: 2026-03-26T08:06:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR E86-87)
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR E86-87)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/663",
    "number": "663",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001055",
        "district": "1",
        "firstName": "Ed",
        "fullName": "Rep. Case, Ed [D-HI-1]",
        "lastName": "Case",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "To oppose the permitting of deep seabed mining and exploration for deep seabed mining, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:48Z",
    "updateDateIncludingText": "2026-03-26T08:06:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E86-87)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:10:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
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
      "sponsorshipDate": "2025-01-23",
      "state": "MI"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr663ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 663\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Case (for himself, Ms. Bonamici , Ms. Norton , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo oppose the permitting of deep seabed mining and exploration for deep seabed mining, and for other purposes.\n#### 1. Opposition to permitting of deep seabed mining and exploration for deep seabed mining\n##### (a) Findings\nCongress finds the following:\n**(1)**\nAs determined by the United Nations, most recently in its Sustainable Development Goals report, our world\u2019s oceans are at great risk from a number of factors, including atmospheric change, resource extraction and pollution.\n**(2)**\nThe United Nation\u2019s 2030 Agenda for Sustainable Development, launched by the 2015 UN Summit in New York established Sustainable Development Goal 14 (SDS 14), to conserve and sustainably use the oceans, seas and marine resources. Target 2 of SDS 14 commits States to sustainably manage marine ecosystems to avoid significant adverse impacts and strengthen their resilience.\n**(3)**\nThe international marine scientific and policy consensus is that deep seabed mining presents a major risk to the marine environment, including: the direct loss of unique and ecologically important species; large sediment plumes that will negatively affect ecosystems well beyond the actual mining sites; noise pollution that will cause physiological and behavioral stress to marine species; likely contamination of commercially important species of food fish; and likely negative impacts on carbon sequestration dynamics and deep-ocean carbon storage.\n**(4)**\nThe United Nations Convention on Biological Diversity, 15th Conference of Parties, Decision 15/24 encourages member States to ensure that, before deep seabed mineral exploitation is permitted, the related impacts on the marine environment and biodiversity are sufficiently researched and the risks to the marine ecosystem are sufficiently understood, and sufficient regulation and conditions be imposed to ensure that exploitation does not cause harmful effects to the marine environment and biodiversity.\n**(5)**\nThe 2022 United Nations Environment Programme Financial Initiative report on deep seabed mining states that the financing of such activities is not consistent with Sustainable Blue Economy Finance Principles.\n**(6)**\nThere is currently insufficient scientific information on the deep sea and related marine ecosystems to fully and accurately assess the full risks and impacts of deep seabed mining activities.\n##### (b) Sense of congress\nIt is the sense of Congress that\u2014\n**(1)**\nno deep seabed mining should occur in the international seabed area unless and until adoption by the International Seabed Authority of a full and binding regulatory framework in accordance with the United Nations Convention on the Law of the Sea, in particular Article 145 of the Convention;\n**(2)**\nthere is currently insufficient scientific understanding of, and an absence of consensus on, the extent of the risks and impacts of deep seabed mining on ocean and related ecosystems;\n**(3)**\na regulatory framework should only be adopted by the International Seabed Authority on the basis of a comprehensive scientific understanding of, and consensus on, the potential risks and impacts of deep seabed mining on ocean ecosystems and communities and activities reliant on ocean ecosystems, including fisheries, indigenous peoples and coastal communities;\n**(4)**\nsuch a comprehensive scientific understanding and consensus should only be developed on the basis of sufficient scientific baseline information on the full impacts of deep seabed mining on marine and related ecosystems; and\n**(5)**\nno deep seabed mining should be permitted in the international seabed area unless it is conducted in a manner and under a clear and enforceable regulatory framework that effectively protects the marine environment from harmful effects, does not pose a risk to communities reliant on ocean ecosystems and prevents damage to the flora and fauna of the marine environment consistent with the obligations in Article 145 of the United Nations Convention on the Law of the Sea and relevant global commitments for the conservation and sustainable use of the marine environment.\n##### (c) In general\nThe President shall, until such time as the President submits to the appropriate congressional committees a certification described in subsection (d) and a report described in subsection (e), direct the United States representative to each relevant international organization to which the United States is a member or observer to take such actions as may be necessary to use the voice, vote, and influence of the United States in such organization to\u2014\n**(1)**\ncall for a moratorium on the permitting of deep seabed mining and exploration for deep seabed mining; and\n**(2)**\noppose investments in or other financing or support of deep seabed mining and exploration for deep seabed mining.\n##### (d) Certification\nA certification described in this subsection is a certification that\u2014\n**(1)**\ndeep seabed mining regulations have been promulgated by the International Seabed Authority; and\n**(2)**\nsuch regulations\u2014\n**(A)**\nare informed by the scientific consensus on impacts to ocean ecosystems; and\n**(B)**\nwill ensure the effective protection of the marine environment from the harmful effects of deep seabed mining.\n##### (e) Report\nA report described in this subsection is a report that includes the following:\n**(1)**\nThe details of the deep seabed mining regulations promulgated by the International Seabed Authority as described in subsection (d).\n**(2)**\nThe scientific consensus on the risks and impacts of such regulations on ocean ecosystems and communities reliant on ocean ecosystems.\n**(3)**\nThe methods by which such regulations ensure the effective protection of the marine environment from harmful effects of deep seabed mining pursuant to subsection (b)(4).",
      "versionDate": "2025-01-23",
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
        "name": "Energy",
        "updateDate": "2025-03-04T20:20:10Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr663ih.xml"
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
      "title": "To oppose the permitting of deep seabed mining and exploration for deep seabed mining, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:27Z"
    },
    {
      "title": "To oppose the permitting of deep seabed mining and exploration for deep seabed mining, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T09:05:30Z"
    }
  ]
}
```
