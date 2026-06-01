# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4425?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4425
- Title: No Immunity for Glyphosate Act
- Congress: 119
- Bill type: S
- Bill number: 4425
- Origin chamber: Senate
- Introduced date: 2026-04-28
- Update date: 2026-05-27T21:11:20Z
- Update date including text: 2026-05-27T21:11:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in Senate
- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-04-28: Introduced in Senate

## Actions

- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4425",
    "number": "4425",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "No Immunity for Glyphosate Act",
    "type": "S",
    "updateDate": "2026-05-27T21:11:20Z",
    "updateDateIncludingText": "2026-05-27T21:11:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T22:43:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NJ"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "OR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "VT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4425is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4425\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2026 Mr. Heinrich (for himself, Mr. Booker , Mr. Markey , Mr. Merkley , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo prohibit the use of Federal funds to implement the Executive order entitled Promoting the National Defense by Ensuring an Adequate Supply of Elemental Phosphorus and Glyphosate-Based Herbicides , and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Immunity for Glyphosate Act .\n#### 2. Prohibition on use of funds for Executive Order relating to phosphorus and glyphosate-based herbicides\nNo Federal funds may be obligated or expended to implement, administer, or enforce Executive Order 14387 (91 Fed. Reg. 8703; relating to promoting the national defense by ensuring an adequate supply of elemental phosphorus and glyphosate-based herbicides).\n#### 3. No immunities for glyphosate manufacturers\n##### (a) Cause of action\nAny person, or the estate, survivors, or legal representative of such person, who suffers or has suffered physical injury, illness, disease, or death caused, in whole or in part, by exposure to elemental phosphorus or a glyphosate-based herbicide manufactured, distributed, sold, or supplied within the United States, may bring a civil action in an appropriate district court of the United States against any covered entity.\n##### (b) Covered entities\nFor purposes of this section, the term covered entity means any person, corporation, partnership, association, contractor, subcontractor, or other entity that manufactures, distributes, formulates, supplies, or sells elemental phosphorus or glyphosate-based herbicides.\n##### (c) Jurisdiction\nThe district courts of the United States shall have jurisdiction over any civil action arising under this section without regard to the amount in controversy or the citizenship of the parties.\n##### (d) Relief\nIn a civil action under this section, the court may award\u2014\n**(1)**\ncompensatory damages, including damages for medical expenses, lost income, pain and suffering, and wrongful death;\n**(2)**\npunitive damages;\n**(3)**\nequitable relief, including declaratory and injunctive relief; and\n**(4)**\nattorney\u2019s fees and costs.\n##### (e) Waiver and nullification of immunity\nNotwithstanding section 707 of the Defense Production Act of 1950 ( 50 U.S.C. 4557 ) or any other provision of law, no covered entity shall be immune from civil liability under Federal or State law for injury, illness, disease, or death caused by exposure to elemental phosphorus or glyphosate-based herbicides.\n##### (f) No Federal contractor defense\nNotwithstanding any other provision of Federal law, including any doctrine of Federal contractor immunity or preemption, no covered entity may assert as a defense to liability in any action brought under this section, or under any other Federal or State law, that the manufacture, formulation, distribution, sale, or supply of elemental phosphorus or a glyphosate-based herbicide was conducted in compliance with, or pursuant to, an Executive order, regulation, directive, contract, or other authorization issued under the Defense Production Act of 1950 ( 50 U.S.C. 4501 et seq. ), or any other Federal law, regulation, or authority.\n##### (g) Preservation of existing and pending claims\nNothing in this Act shall be construed to\u2014\n**(1)**\npreempt, displace, or otherwise limit any civil action authorized under Federal or State law; or\n**(2)**\nrequire dismissal of, or otherwise adversely affect, any civil action pending on or before the date of enactment of this Act.\n##### (h) Applicability\nThis section shall apply to any claim arising before, on, or after the date of enactment of this Act.\n##### (i) Non-Preemption of state law\nNothing in this section shall be construed to preempt, displace, or limit any right or remedy available under State law.",
      "versionDate": "2026-04-28",
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
        "actionDate": "2026-02-20",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7601",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Immunity for Glyphosate Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-05-20T19:11:24Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4425is.xml"
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
      "title": "No Immunity for Glyphosate Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Immunity for Glyphosate Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of Federal funds to implement the Executive order entitled \"Promoting the National Defense by Ensuring an Adequate Supply of Elemental Phosphorus and Glyphosate-Based Herbicides\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T04:18:39Z"
    }
  ]
}
```
