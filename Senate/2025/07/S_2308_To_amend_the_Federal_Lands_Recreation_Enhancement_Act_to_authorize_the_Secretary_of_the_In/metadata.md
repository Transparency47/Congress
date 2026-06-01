# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2308?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2308
- Title: PATRIOT Parks Act
- Congress: 119
- Bill type: S
- Bill number: 2308
- Origin chamber: Senate
- Introduced date: 2025-07-16
- Update date: 2026-04-02T21:21:13Z
- Update date including text: 2026-04-02T21:21:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in Senate
- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- Latest action: 2025-07-16: Introduced in Senate

## Actions

- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2308",
    "number": "2308",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "PATRIOT Parks Act",
    "type": "S",
    "updateDate": "2026-04-02T21:21:13Z",
    "updateDateIncludingText": "2026-04-02T21:21:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T21:16:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T18:13:15Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "AR"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "MO"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2308is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2308\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mr. Banks (for himself and Mr. Cotton ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Federal Lands Recreation Enhancement Act to authorize the Secretary of the Interior to collect a surcharge from international visitors to units of the National Park System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting America\u2019s Treasures by Raising Inflow from Overseas Tourists Parks Act or the PATRIOT Parks Act .\n#### 2. Surcharge for international visitors to units of the National Park System\n##### (a) Entrance fee surcharge\nSection 803(e) of the Federal Lands Recreation Enhancement Act ( 16 U.S.C. 6802(e) ) is amended by adding at the end the following:\n(3) Entrance fee surcharge for international visitors (A) Definition of international visitor In this paragraph, the term international visitor means a nonimmigrant individual admitted into the United States under\u2014 (i) section 101(a)(15)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(B) ); or (ii) section 217 of the Immigration and Nationality Act ( 8 U.S.C. 1187 ). (B) Entrance fee surcharge (i) In general For any unit of the National Park System for which an entrance fee is charged, the Secretary may, at the election of the Secretary, or shall, on request of the superintendent of the applicable unit of the National Park System, authorize the superintendent of the applicable unit of the National Park System to establish for any international visitors charged the entrance fee a surcharge in an amount established by the superintendent of the applicable unit of the National Park System, by regulation, to be collected by the Secretary in accordance with this paragraph. (ii) Determination of surcharge amount In establishing the amount of a surcharge under clause (i), the superintendent of the applicable unit of the National Park System shall ensure that the amount maximizes revenue for the applicable unit of the National Park System while retaining international visitation at the applicable unit of the National Park System. (iii) Per-vehicle fee In a case in which an entrance fee to a unit of the National Park System subject to a surcharge under clause (i) is a per-vehicle charge, the Secretary shall establish, by regulation, a process for the superintendent of the applicable unit of the National Park System to proportionately levy and collect the surcharge from international visitors under that clause. (iv) Methods of collection A surcharge established under clause (i) shall be collected\u2014 (I) by the Secretary, using the standard methods by which entrance fees may be collected for a unit of the National Park System under this section; and (II) if the Secretary enters into an agreement with a third-party travel vendor to provide for the collection of the surcharge, by the applicable third-party travel vendor, in accordance with the agreement. (v) Suspension or modification; increase (I) Suspension or modification At the election of the Secretary or on request of the superintendent of a unit of the National Park System at which a surcharge is established under clause (i), the Secretary may suspend the collection of, or otherwise modify, the surcharge for the applicable unit of the National Park System, including providing for tiered pricing of the surcharge based on visitation levels at the unit of the National Park System, as determined appropriate by the Secretary. (II) Increase The Secretary may establish a minimum percentage increase that shall apply to a surcharge established by a superintendent under clause (i) within an applicable timeframe established by the Secretary. (vi) Visa fees; administration A surcharge established under clause (i)\u2014 (I) shall be in addition to, and separate from, any statutory immigrant visa fee charged to an international visitor; and (II) shall not be subject to administration by the Secretary of State or the Secretary of Homeland Security. (vii) Disposition of proceeds Notwithstanding any other provision of law, all proceeds from a surcharge on international visitors collected under this paragraph shall be retained by the applicable unit of the National Park System at which the surcharge was collected, to be distributed by the Secretary for maintenance, visitor services, staffing, and related needs at the unit of the National Park System, as determined appropriate by the Secretary. .\n##### (b) Recreation passes\nSection 805(a) of the Federal Lands Recreation Enhancement Act ( 16 U.S.C. 6804(a) ) is amended by adding at the end the following:\n(11) Surcharge for certain international visitors (A) In general The Secretary shall establish, by regulation, a surcharge to be collected from the sale of any National Parks and Federal Recreational Lands Pass to an international visitor (as defined in section 803(e)(3)(A)), the amount of which may be increased by the Secretary in a percentage and in a timeframe determined to be reasonable by the Secretary. (B) Disposition of proceeds Notwithstanding any other provision of law, any amounts collected as a surcharge under subparagraph (A) shall be deposited in the National Parks and Public Land Legacy Restoration Fund established by section 200402(a) of title 54, United States Code. .",
      "versionDate": "2025-07-16",
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
        "actionDate": "2025-07-22",
        "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4604",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting America\u2019s Treasures by Raising Inflow from Overseas Tourists (PATRIOT) Parks Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-01-07T16:55:52Z"
          },
          {
            "name": "Travel and tourism",
            "updateDate": "2026-01-07T16:56:01Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2026-01-07T16:55:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-18T16:03:08Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2308is.xml"
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
      "title": "PATRIOT Parks Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PATRIOT Parks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting America\u2019s Treasures by Raising Inflow from Overseas Tourists Parks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Land Recreation Enhancement Act to authorize the Secretary of the Interior to collect a surcharge from international visitors to units of the National Park System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:33:47Z"
    }
  ]
}
```
