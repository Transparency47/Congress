# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7140?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7140
- Title: CLEAR Act
- Congress: 119
- Bill type: HR
- Bill number: 7140
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-02-12T15:22:35Z
- Update date including text: 2026-02-12T15:22:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7140",
    "number": "7140",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "CLEAR Act",
    "type": "HR",
    "updateDate": "2026-02-12T15:22:35Z",
    "updateDateIncludingText": "2026-02-12T15:22:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
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
          "date": "2026-01-16T20:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7140ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7140\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Ms. Lee of Florida (for herself and Ms. Lofgren ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo protect main street retailers and end users in secondary patent actions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Customer Legal Ease and Relief Act or the CLEAR Act .\n#### 2. Stay of action against retailer or end user\n##### (a) Amendment\nChapter 29 of title 35, United States Code, is amended by adding at the end the following:\n299A. Stay of action against retailer or end user (a) Entry of stay In a civil action in which a party asserts a claim for relief for infringement of a patent, the court shall grant a motion to stay at least the portion of the action against a retailer or end user of an accused instrumentality if\u2014 (1) the manufacturer of the accused instrumentality is a party to the action or a separate action involving the patent and the accused instrumentality; (2) the retailer or end user does not manufacture, assemble, integrate, or transform the accused instrumentality or a relevant part thereof; (3) the retailer or end user agrees that if a final judgment on the merits is entered in the action to which the manufacturer is a party, for any future action involving the same accused instrumentality supplied by the same manufacturer, the retailer or end user\u2014 (A) waives all defenses under section 282(b); and (B) is bound by any issue decided in the action to which the manufacturer is a party; and (4) the retailer or end user agrees to be bound by any injunction issued with respect to the accused instrumentality in the action to which the manufacturer is a party. (b) Lift of stay A stay entered under this section shall be lifted upon a showing that the manufacturer cannot be made to satisfy a damages judgment. (c) Bond or escrow The court may conduct an initial hearing or inquiry to determine if the manufacturer can be made to satisfy a damages judgment. If the court determines that there is a substantial likelihood that the manufacturer will not satisfy a damages judgment, the court may require the retailer or end user to post a bond or place funds or other property in escrow. (d) Stipulation as To use of accused instrumentality The court may, as necessary in view of an infringement claim against the manufacturer, require the end user or retailer to stipulate as to the extent of the use of the accused instrumentality and allow limited discovery as to such use. (e) Time limit A motion for a stay under this section shall be filed not later than the later of\u2014 (1) six months after the service of the first pleading or paper in the action that specifically identifies the accused instrumentality and how the accused instrumentality is alleged to infringe the patent; (2) six months after the date on which the manufacturer becomes a party to an action involving the patent and the accused instrumentality; or (3) the entry of the first scheduling order in the case. (f) Rule of construction Nothing in this section may be construed to limit the discretion of a court to enter a stay under other authority. (g) Definitions In this section: (1) Accused instrumentality The term accused instrumentality means a product, or an instrumentality that implements a process, that is a material part of the claimed invention. (2) Affiliate The term affiliate means any entity that controls, is controlled by, or is under common control of another entity. (3) End user The term end user means an entity that does not use the accused instrumentality other than for the ordinary and intended purpose of the instrumentality and that does not direct, obligate, or induce the manufacturer to make the accused instrumentality. (4) Manufacturer The term manufacturer means an entity that makes, assembles, integrates, transforms, or supplies the accused instrumentality. (5) Retailer The term retailer means an entity that generates revenues predominantly through the sale to the public of consumer goods or services, or an affiliate of such entity. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 29 of title 35, United States Code, is amended by adding at the end the following new item:\nSec. 299A. Stay of action against retailer or end user. .\n##### (c) Effective date\nThe amendments made by this Act shall take effect on the date of the enactment of this Act and shall apply to any action for which a complaint is served on and after such effective date.",
      "versionDate": "2026-01-16",
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
        "name": "Commerce",
        "updateDate": "2026-02-12T15:22:34Z"
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
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7140ih.xml"
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
      "title": "CLEAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLEAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Customer Legal Ease and Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect main street retailers and end users in secondary patent actions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T04:48:22Z"
    }
  ]
}
```
