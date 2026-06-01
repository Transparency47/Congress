# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7159?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7159
- Title: Protecting Local Zoos Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7159
- Origin chamber: House
- Introduced date: 2026-01-20
- Update date: 2026-04-10T23:50:07Z
- Update date including text: 2026-04-10T23:50:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-20: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-01-28 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-02-04 - Committee: Subcommittee Hearings Held
- Latest action: 2026-01-20: Introduced in House

## Actions

- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-01-28 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-02-04 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-20",
    "latestAction": {
      "actionDate": "2026-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7159",
    "number": "7159",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "G000565",
        "district": "9",
        "firstName": "Paul",
        "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
        "lastName": "Gosar",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Protecting Local Zoos Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-10T23:50:07Z",
    "updateDateIncludingText": "2026-04-10T23:50:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-28",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-20",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-20",
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
          "date": "2026-01-20T17:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-04T15:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-01-28T18:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "FL"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7159ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7159\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2026 Mr. Gosar introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Lacey Act Amendments of 1981 to adjust provisions relating to captive wildlife offenses.\n#### 1. Short title\nThis Act may be cited as the Protecting Local Zoos Act of 2026 .\n#### 2. Amendments to captive wildlife offenses under Lacey Act Amendments of 1981\n##### (a) In general\nSection 3(e) of the Lacey Act Amendments of 1981 ( 16 U.S.C. 3372(e) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking in paragraph (2) and inserting in paragraphs (2) and (3) ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby inserting an entity licensed to hold animals under a Class B license from the Department of Agriculture, before an entity exhibiting animals ;\n**(ii)**\nin clause (i)\u2014\n**(I)**\nin subclause (I), by inserting , including an owner, executive, or volunteer, after or contractor ; and\n**(II)**\nin subclause (II), by inserting or other veterinary or medical professional, such as a veterinary assistant, veterinary technician, or non-veterinary specialist after veterinarian) ; and\n**(iii)**\nin clause (ii), by striking snow leopard (Uncia uncia), ;\n**(B)**\nin subparagraph (D), by striking or at the end;\n**(C)**\nin subparagraph (E)(iii), by striking the period at the end and inserting ; or ; and\n**(D)**\nby adding at the end the following:\n(F) a person described in subparagraph (A), (B), or (C) that is in possession of any prohibited wildlife species and\u2014 (i) registers each individual animal of each prohibited wildlife species possessed by the person with the United States Fish and Wildlife Service; and (ii) beginning on the date of such registration, does not\u2014 (I) breed, acquire, or sell any prohibited wildlife species; (II) allow direct contact between the public and any prohibited wildlife species; and (III) exhibit to the public any prohibited wildlife species. ; and\n**(3)**\nby adding at the end the following:\n(3) Export and import to foreign entities Notwithstanding paragraph (1), an entity or a facility described in paragraph (2)(A) that is in compliance with the requirements of that paragraph may export to or import from a foreign entity that is authorized to operate in the country within which it is located and is lawfully operating in such country at the time of such export or import a prohibited wildlife species. (4) Cancellation of mistaken registration (A) In general A covered registered entity or individual may submit to the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service, an application to cancel the registration under paragraph (2)(E) of such covered registered entity or individual. (B) Application requirement A covered registered entity or individual shall include in an application submitted under subparagraph (A) evidence sufficient for the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service, to determine that the covered registered entity or individual qualifies for an exception from the application of paragraph (1) pursuant to subparagraph (A), (B), or (C) of paragraph (2) as of the date on which the covered registered entity or individual\u2014 (i) registered with the United States Fish and Wildlife Service under paragraph (2)(E); and (ii) submits such application. (C) Grant of application If the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service, makes an affirmative determination under subparagraph (B) with respect to an application submitted by a covered registered entity or individual under subparagraph (A), the Director shall grant such application. (D) Covered registered entity or individual defined In this paragraph, the term covered registered entity or individual means an entity or individual described in paragraph (2)(E) that\u2014 (i) is in compliance with the requirements of that paragraph; (ii) registered with the United States Fish and Wildlife Service as described in that paragraph; and (iii) would have, on the date of such registration, qualified for an exception from the application of paragraph (1) pursuant to subparagraph (A), (B), or (C) of paragraph (2). .\n##### (b) Definition of prohibited wildlife species\nSection 2(h) of the Lacey Act Amendments of 1981 ( 16 U.S.C. 3371(h) ) is amended\u2014\n**(1)**\nby striking The term and inserting the following:\n(1) In general The term ; and\n**(2)**\nby adding at the end the following:\n(2) Exclusions The term prohibited wildlife species does not include the snow leopard ( Uncia uncia ) or the clouded leopard ( Neofelis nebulosa ) or any hybrid of either such species. .",
      "versionDate": "2026-01-20",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2026-03-09T16:47:19Z"
          },
          {
            "name": "Crimes against animals and natural resources",
            "updateDate": "2026-03-09T16:52:33Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-03-09T16:48:42Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2026-03-09T16:49:11Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-03-09T16:49:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Animals",
        "updateDate": "2026-04-10T23:50:07Z"
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
      "date": "2026-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7159ih.xml"
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
      "title": "Protecting Local Zoos Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Local Zoos Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Lacey Act Amendments of 1981 to adjust provisions relating to captive wildlife offenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:33:53Z"
    }
  ]
}
```
