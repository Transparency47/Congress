# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6342?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6342
- Title: Clean Up DEBRIS Act
- Congress: 119
- Bill type: HR
- Bill number: 6342
- Origin chamber: House
- Introduced date: 2025-12-01
- Update date: 2026-02-03T09:05:23Z
- Update date including text: 2026-02-03T09:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-12-01: Introduced in House

## Actions

- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6342",
    "number": "6342",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Clean Up DEBRIS Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:23Z",
    "updateDateIncludingText": "2026-02-03T09:05:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-01",
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
      "actionDate": "2025-12-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-01",
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
          "date": "2025-12-01T17:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:26:19Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6342ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6342\nIN THE HOUSE OF REPRESENTATIVES\nDecember 1, 2025 Mr. Steube (for himself and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide assistance for common interest communities, condominiums, and housing cooperatives damaged by a major disaster, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clean Up Disasters and Emergencies with Better Recovery and Immediate Support Act or the Clean Up DEBRIS Act .\n#### 2. Definitions\nSection 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ) is amended by adding at the end the following:\n(13) Residential common interest community The term residential common interest community means any mandatory membership organization comprising owners of real estate described in a declaration or created pursuant to a covenant or other applicable law with respect to which a person, by virtue of the person\u2019s ownership of a unit, is obligated to pay for a share of real estate taxes, insurance premiums, maintenance, or improvement of, or services or other expenses related to, common elements, other units, or any other real estate other than that unit described in the declaration. (14) Condominium The term condominium means a stand-alone condominium project in which each dwelling unit is separately owned, in which the remaining portions of the real estate are designated for common ownership solely by the owners of the related units, each owner having an undivided interest in the common elements, and which is represented by an association consisting exclusively of all the unit owners in the project, which is, or will be responsible for the operation, administration, and management of the project. (15) Housing cooperative The term housing cooperative means a multi-unit housing entity, including an association of manufactured homes, in which each dwelling unit is subject to separate use and possession by 1 or more cooperative members whose interest in such unit, and in any undivided assets of the cooperative association that are appurtenant to such unit, is evidenced by a membership or share interest in a cooperative association and a lease or other document of title or possession granted by such cooperative as the owner of all cooperative property. (16) Manufactured home park The term manufactured home park means a parcel (or contiguous parcels) of land divided into 2 or more lots containing manufactured home structures, regardless of whether such structures are taxed as real property, that are\u2014 (A) transportable in 1 or more sections; (B) built on a permanent chassis and is designed for use with or without a permanent foundation when attached to the required utilities; and (C) affixed to land. .\n#### 3. Removal of debris resulting from a major disaster in residential common interest communities\nSection 407 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5173 ) is amended\u2014\n**(1)**\nby redesignating subsections (d) and (e) as subsections (e) and (f); and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Rules relating to residential common interest communities (1) Issuance of rules The President shall issue rules which provide that removal of debris or wreckage from a unit of real estate within a residential common interest community, condominium entity, an entity of a housing cooperative, or a manufactured home park from a major disaster is in the public interest when a State or local government determines in writing such debris or wreckage constitutes a threat to life, to public health or safety, or to the economic recovery of the residential common interest community. (2) Deference In issuing the rules under paragraph (1), the President shall be deferential to defined terms in State or local laws and ordinances. .\n#### 4. Applicability\nThe amendments made by this Act shall apply to a major disaster or emergency declared by the President under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ) on or after the date of enactment of this Act.",
      "versionDate": "2025-12-01",
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
        "name": "Emergency Management",
        "updateDate": "2025-12-11T15:08:04Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6342ih.xml"
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
      "title": "Clean Up DEBRIS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clean Up DEBRIS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T07:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clean Up Disasters and Emergencies with Better Recovery and Immediate Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T07:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide assistance for common interest communities, condominiums, and housing cooperatives damaged by a major disaster, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-11T07:18:28Z"
    }
  ]
}
```
