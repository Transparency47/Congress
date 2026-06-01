# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7187?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7187
- Title: Clarity for Compensation Act
- Congress: 119
- Bill type: HR
- Bill number: 7187
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-04-15T08:05:54Z
- Update date including text: 2026-04-15T08:05:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7187",
    "number": "7187",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Clarity for Compensation Act",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:54Z",
    "updateDateIncludingText": "2026-04-15T08:05:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
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
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:03:10Z",
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
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7187ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7187\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Mr. Nunn of Iowa (for himself and Mr. Meeks ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Securities Exchange Act of 1934 to provide an exemption from the definition of a broker for a certain registered representative-owned personal services entity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clarity for Compensation Act .\n#### 2. Broker definition exception for registered representative-owned personal services entity\n##### (a) In general\nSection 3(a)(4) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a)(4) ) is amended by adding at the end the following:\n(G) Exception for registered representative-owned personal services entity (i) In general A personal services entity shall not be considered a broker solely by reason of receiving compensation on behalf of a registered representative from that representative\u2019s broker at the direction of such representative, if\u2014 (I) the broker instructs or otherwise approves the amount and timing of the payment and maintains records regarding the payment made; (II) the personal services entity does not hold itself out as a broker; (III) the personal services entity does not engage in broker or dealer activity, other than the receipt of compensation on behalf of the registered representative; (IV) the broker maintains adequate supervision and control over the registered representative; (V) the broker and the personal services entity have a written agreement governing their relationship and the responsibilities of each party regarding compensation arrangements; (VI) the personal services entity is only owned by\u2014 (aa) the registered representative; (bb) if the registered representative is an individual, immediate family members of the registered representative; or (cc) entities wholly owned by\u2014 (AA) the registered representative; or (BB) if the registered representative is an individual, immediate family members of the registered representative; and (VII) the personal services entity meets such other requirements as the Commission may prescribe, by rule. (ii) Oversight and examination In order to ensure that a personal services entity that is not considered a broker by reason of this subparagraph continues to meet the requirements to not be considered a broker by reason of this subparagraph, the personal services entity shall maintain, and make available upon request to the Commission and the applicable self-regulatory organization, all books and records that both\u2014 (I) the broker from which the personal services entity receives compensation is required to maintain and make available to the Commission and the applicable self-regulatory organization; and (II) the Commission determines necessary and appropriate to demonstrate that the personal services entity continues to meet the requirements to not be considered a broker by reason of this subparagraph. (iii) Definitions In this subparagraph: (I) Applicable self-regulatory organization With respect to a personal services entity or a registered representative of a broker, the term applicable self-regulatory organization means each self-regulatory organization with which the related broker is required to be registered. (II) Broker or dealer activity The term broker or dealer activity means an activity undertaken by a broker or a dealer who is registered, or required to be registered, under this Act. (III) Immediate family member With respect to an individual, the term immediate family member means a spouse, child, parent, brother, sister, grandparent, grandchild, stepparent, stepchild, stepbrother, or stepsister of the individual. (IV) Personal services entity The term personal services entity means an entity that is established by a registered representative to receive compensation for the services of the registered representative and for administrative purposes and other benefits. (V) Registered representative With respect to a broker, the term registered representative means a person who is\u2014 (aa) an associated person of a broker or dealer with respect to the broker; and (bb) registered with the applicable self-regulatory organization. .\n##### (b) Effective date\nSection 3(a)(4)(G) of the Securities Exchange Act of 1934, as added by subsection (a), shall take effect on the date that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2026-01-21",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-02-18T16:58:00Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7187ih.xml"
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
      "title": "To amend the Securities Exchange Act of 1934 to provide an exemption from the definition of a broker for a certain registered representative-owned personal services entity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T09:06:14Z"
    },
    {
      "title": "Clarity for Compensation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clarity for Compensation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:38:21Z"
    }
  ]
}
```
