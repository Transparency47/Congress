# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1946?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1946
- Title: 45Q Repeal Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1946
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-05-08T14:00:47Z
- Update date including text: 2025-05-08T14:00:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1946",
    "number": "1946",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "45Q Repeal Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-08T14:00:47Z",
    "updateDateIncludingText": "2025-05-08T14:00:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:02:25Z",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1946ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1946\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Perry (for himself and Mr. Khanna ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal the carbon oxide sequestration credit.\n#### 1. Short title\nThis Act may be cited as the 45Q Repeal Act of 2025 .\n#### 2. Repeal of carbon oxide sequestration credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by repealing section 45Q and by striking the item relating to such section from the table of sections for such subpart.\n##### (b) Conforming amendments\n**(1)**\nSection 38(b) is amended by striking paragraph (29).\n**(2)**\nSection 45V(d) is amended by striking paragraph (2).\n**(3)**\nSection 48(a)(15) is amended\u2014\n**(A)**\nin subparagraph (B), by striking or section 45Q , and\n**(B)**\nin subparagraph (C)(ii)(I), by striking or 45Q .\n**(4)**\nSection 45Y(b)(1)(D) is amended by striking 45Q, .\n**(5)**\nSection 45Y(b)(2)(D) is amended to read as follows:\n(D) Carbon capture and sequestration equipment (i) In general For purposes of this subsection, the amount of greenhouse gases emitted into the atmosphere by a facility in the production of electricity shall not include any qualified carbon dioxide that is captured by the taxpayer and\u2014 (I) pursuant to any regulations established under clause (ii), disposed of by the taxpayer in secure geological storage, or (II) utilized by the taxpayer in a manner described in paragraph (5) of such section. (ii) Regulations (I) In general The Secretary, in consultation with the Administrator of the Environmental Protection Agency, the Secretary of Energy, and the Secretary of the Interior, shall establish regulations for determining adequate security measures for the geological storage of qualified carbon oxide under clause (i) such that the qualified carbon oxide does not escape into the atmosphere. Such term shall include storage at deep saline formations, oil and gas reservoirs, and unminable coal seams under such conditions as the Secretary may determine under such regulations. (II) Qualified carbon oxide For purposes of this clause, the term qualified carbon oxide has the meaning given such term in section 45Q(c) as such section was in effect on the day before the date of the enactment of the 45Q Repeal Act of 2025 . .\n**(6)**\nSection 45Z(d)(4)(B) is amended by striking clause (iii).\n**(7)**\nSection 48C(f) is amended by striking 45Q, .\n**(8)**\nSection 48E(b)(3)(C) is amended by striking clause (iii).\n**(9)**\nSection 142(o)(1)(B) is amended by inserting , as such section was in effect on the day before the date of the enactment of the 45Q Repeal Act of 2025 after 45Q(e)(3) .\n**(10)**\nSection 6417 is amended\u2014\n**(A)**\nin subsection (b) by striking paragraph (3), and\n**(B)**\nin subsection (d)\u2014\n**(i)**\nin paragraph (1)(C), by inserting , as such section was in effect on the day before the date of the enactment of the 45Q Repeal Act of 2025 after 45Q(d) , and\n**(ii)**\nin paragraph (3)(C)(i)(II)(bb), by striking period described in paragraph (3)(A) or (4)(A) of section 45Q(a) with respect to such equipment and inserting 12-year period beginning on the date the equipment was originally placed in service .\n**(11)**\nSection 6418(f)(1)(A) is amended by striking clause (iii).\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-03-06",
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
        "updateDate": "2025-05-08T14:00:47Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1946ih.xml"
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
      "title": "45Q Repeal Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "45Q Repeal Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to repeal the carbon oxide sequestration credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:19Z"
    }
  ]
}
```
