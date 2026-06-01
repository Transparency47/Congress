# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6376?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6376
- Title: Supporting Military Families Exposed to Toxic Substances Act
- Congress: 119
- Bill type: HR
- Bill number: 6376
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-01-09T09:06:47Z
- Update date including text: 2026-01-09T09:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6376",
    "number": "6376",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Supporting Military Families Exposed to Toxic Substances Act",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:47Z",
    "updateDateIncludingText": "2026-01-09T09:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-05",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-05T14:11:35Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MI"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "FL"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "KY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6376ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6376\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Ms. Brownley (for herself and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide health care for family members and other individuals who resided at or worked at locations where there is a presumption of service-connection for certain illnesses and conditions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Military Families Exposed to Toxic Substances Act .\n#### 2. Department of Veterans Affairs provision of health care for family members and other individuals who resided at or worked at locations where there is a presumption of service-connection for certain illnesses and conditions\n##### (a) In general\nSubchapter VIII of chapter 17 of title 38, United States Code, is amended by adding at the end the following new section:\n1790. Health care for family members and other individuals who resided at or worked at locations where there is a presumption of service-connection for certain illnesses and conditions (a) In general (1) An individual described in subsection (b) shall be eligible for hospital care and medical services furnished by the Secretary for a covered illness or condition. (2) An individual described in this subsection is an individual who\u2014 (A) resided at, worked at, or was in utero while their mother resided at or worked at a location for which the Secretary has established a presumption of service-connection for any illness or condition under or pursuant to chapter 11 of this title for the time period required for such presumption; and (B) can demonstrate that the individual was exposed to the same condition or conditions that qualify veterans for such presumption, as determined by the Secretary. (b) Limitations (1) The Secretary may only furnish hospital care and medical services under subsection (a) to the extent and in the amount provided in advance in appropriations Acts for such purpose. (2) Hospital care and medical services may not be furnished under subsection (a) for an illness or condition of an individual that is found, in accordance with guidelines issued by the Under Secretary for Health, to have resulted from a cause other than time spent at a location referred to in subsection (a)(2)(A). (3) The Secretary may furnish hospital care or medical services provided to an individual described in subsection (a)(2) only after the individual or the provider of such care or services has exhausted without success all claims and remedies reasonably available to the individual or provider against a third party (as defined in section 1725(f) of this title) for payment of such care or services, including with respect to health-plan contracts (as defined in such section). (c) Covered illness or condition In this section, the term covered illness or condition means, with respect to an individual who resided at, worked at, or was in utero while their mother resided at or worked at a location, an illness or condition for which the Secretary has established a presumption of service-connection under or pursuant to chapter 11 of this title based on service in the Armed Forces at that location, notwithstanding that there is insufficient medical evidence to conclude that the illness or condition is attributable to such residence or work. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1789 the following new item:\n1790. Health care for family members and other individuals who resided at or worked at locations where there is a presumption of service-connection for certain illnesses and conditions. .\n##### (c) Reports\nNot later than December 31 of each of 2027, 2028, and 2029, the Secretary of Veterans Affairs shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the hospital care and medical services provided under section 1790 of title 38, United States Code, as added by subsection (a). Each such report shall include each of the following:\n**(1)**\nThe number of individuals who were furnished hospital care or medical services under such section during the period beginning on January 1, 2026, and ending on the date of such report.\n**(2)**\nThe illnesses and conditions for which such care or services were provided and the location associated with the presumption of service-connection for each such illness or condition.\n**(3)**\nThe number of individuals who applied for care or services under such section during that period but who were denied, including information on the reasons for such denials.\n**(4)**\nThe number of individuals who applied for care or services under such section and are awaiting a decision from the Secretary on eligibility for such care or services. as of the date of such report.",
      "versionDate": "2025-12-03",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T16:22:31Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6376ih.xml"
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
      "title": "Supporting Military Families Exposed to Toxic Substances Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-24T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Military Families Exposed to Toxic Substances Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide health care for family members and other individuals who resided at or worked at locations where there is a presumption of service-connection for certain illnesses and conditions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-24T04:03:24Z"
    }
  ]
}
```
