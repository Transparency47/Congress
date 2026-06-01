# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7601?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7601
- Title: No Immunity for Glyphosate Act
- Congress: 119
- Bill type: HR
- Bill number: 7601
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-05-27T21:11:19Z
- Update date including text: 2026-05-27T21:11:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7601",
    "number": "7601",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "No Immunity for Glyphosate Act",
    "type": "HR",
    "updateDate": "2026-05-27T21:11:19Z",
    "updateDateIncludingText": "2026-05-27T21:11:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
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
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
          "date": "2026-02-20T16:34:15Z",
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
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "ME"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "CO"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "SC"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "CT"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "FL"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "TN"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7601ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7601\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. Massie (for himself, Ms. Pingree , Ms. Boebert , Ms. Mace , and Mr. Khanna ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit the use of Federal funds to implement the Executive order entitled Promoting the National Defense by Ensuring an Adequate Supply of Elemental Phosphorus and Glyphosate-Based Herbicides , and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Immunity for Glyphosate Act .\n#### 2. No federal funds for executive order relating to phosphorus and glyphosate-based herbicides\nNo Federal funds may be used to implement, administer, or enforce the Executive order entitled Promoting the National Defense by Ensuring an Adequate Supply of Elemental Phosphorus and Glyphosate-Based Herbicides , issued on February 18, 2026.\n#### 3. No immunities for glyphosate manufacturers\n##### (a) Cause of action\nAny person, or the estate, survivors, or legal representative of such person, who suffers or has suffered physical injury, illness, disease, or death caused, in whole or in part, by exposure to elemental phosphorus or a glyphosate-based herbicide manufactured, distributed, sold, or supplied within the United States, may bring a civil action in an appropriate district court of the United States against any covered entity.\n##### (b) Covered entities\nFor purposes of this section, the term covered entity means any person, corporation, partnership, association, contractor, subcontractor, or other entity that manufactures, distributes, formulates, supplies, or sells elemental phosphorus or glyphosate-based herbicides.\n##### (c) Jurisdiction\nThe district courts of the United States shall have jurisdiction over any civil action arising under this section without regard to the amount in controversy or the citizenship of the parties.\n##### (d) Relief\nIn a civil action under this section, the court may award\u2014\n**(1)**\ncompensatory damages, including damages for medical expenses, lost income, pain and suffering, and wrongful death;\n**(2)**\npunitive damages;\n**(3)**\nequitable relief, including declaratory and injunctive relief; and\n**(4)**\nattorney\u2019s fees and costs.\n##### (e) Waiver and nullification of immunity\nNotwithstanding section 707 of the Defense Production Act of 1950 ( 50 U.S.C. 4557 ), or any other provision of law, no covered entity shall be immune from civil liability under Federal or State law for injury, illness, disease, or death caused by exposure to elemental phosphorus or glyphosate-based herbicides.\n##### (f) No federal contractor defense\nNotwithstanding any other provision of Federal law, including any doctrine of Federal contractor immunity or preemption, no covered entity may assert as a defense to liability in any action brought under this section, or under any other Federal or State law, that the manufacture, formulation, distribution, sale, or supply of elemental phosphorus or a glyphosate-based herbicide was conducted in compliance with, or pursuant to, an Executive order, regulation, directive, contract, or other authorization issued under the Defense Production Act of 1950 ( 50 U.S.C. 4501 et seq. ), or any other Federal law, regulation, or authority.\n##### (g) Preservation of existing and pending claims\nNothing in this Act shall be construed to\u2014\n**(1)**\npreempt, displace, or otherwise limit any civil action authorized under Federal or State law; or\n**(2)**\nrequire dismissal of, or otherwise adversely affect, any civil action pending on or before the date of enactment of this Act.\n##### (h) Applicability\nThis section shall apply to any claim arising before, on, or after the date of enactment of this Act.\n##### (i) Non-Preemption of state law\nNothing in this section shall be construed to preempt, displace, or limit any right or remedy available under State law.",
      "versionDate": "2026-02-20",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-04-28",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "4425",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Immunity for Glyphosate Act",
      "type": "S"
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
        "name": "Health",
        "updateDate": "2026-03-06T20:24:39Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7601ih.xml"
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
      "title": "No Immunity for Glyphosate Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-04T03:08:22Z"
    },
    {
      "title": "No Immunity for Glyphosate Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-04T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of Federal funds to implement the Executive order entitled \"Promoting the National Defense by Ensuring an Adequate Supply of Elemental Phosphorus and Glyphosate-Based Herbicides\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-04T03:03:24Z"
    }
  ]
}
```
