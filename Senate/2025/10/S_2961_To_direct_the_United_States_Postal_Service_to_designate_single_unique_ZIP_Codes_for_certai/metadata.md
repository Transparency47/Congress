# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2961?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2961
- Title: A bill to direct the United States Postal Service to designate single, unique ZIP Codes for certain communities, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 2961
- Origin chamber: Senate
- Introduced date: 2025-10-01
- Update date: 2025-12-10T21:58:52Z
- Update date including text: 2025-12-10T21:58:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-01: Introduced in Senate
- 2025-10-01 - IntroReferral: Introduced in Senate
- 2025-10-01 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-10-01: Introduced in Senate

## Actions

- 2025-10-01 - IntroReferral: Introduced in Senate
- 2025-10-01 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-01",
    "latestAction": {
      "actionDate": "2025-10-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2961",
    "number": "2961",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "A bill to direct the United States Postal Service to designate single, unique ZIP Codes for certain communities, and for other purposes.",
    "type": "S",
    "updateDate": "2025-12-10T21:58:52Z",
    "updateDateIncludingText": "2025-12-10T21:58:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-01",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-01",
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
          "date": "2025-10-01T16:39:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "CO"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-10-01",
      "state": "OK"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "CO"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2961is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2961\nIN THE SENATE OF THE UNITED STATES\nOctober 1, 2025 Mr. Banks (for himself, Mr. Bennet , Mr. Mullin , and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo direct the United States Postal Service to designate single, unique ZIP Codes for certain communities, and for other purposes.\n#### 1. Single, unique zip codes for certain communities\nNot later than 270 days after the date of enactment of this Act, the United States Postal Service shall designate a single, unique ZIP Code for each of the following communities:\n**(1)**\nCanyon Lake, California.\n**(2)**\nHidden Hills, California.\n**(3)**\nIndustry, California.\n**(4)**\nNorth Tustin, California.\n**(5)**\nTehachapi, California.\n**(6)**\nCastle Pines, Colorado.\n**(7)**\nCentennial, Colorado.\n**(8)**\nCherry Hills Village, Colorado.\n**(9)**\nFrederick, Colorado.\n**(10)**\nGreenwood Village, Colorado.\n**(11)**\nHighlands Ranch, Colorado.\n**(12)**\nKeystone, Colorado.\n**(13)**\nLone Tree, Colorado.\n**(14)**\nMountain Village, Colorado.\n**(15)**\nSeverance, Colorado.\n**(16)**\nSilver Cliff, Colorado.\n**(17)**\nSterling Ranch, Colorado.\n**(18)**\nSuperior, Colorado.\n**(19)**\nCoconut Creek, Florida.\n**(20)**\nDeerfield Beach, Florida.\n**(21)**\nHollywood, Florida.\n**(22)**\nLighthouse Point, Florida.\n**(23)**\nOakland Park, Florida.\n**(24)**\nParkland, Florida.\n**(25)**\nWilton Manors, Florida.\n**(26)**\nBurr Ridge, Illinois.\n**(27)**\nCarmel, Indiana.\n**(28)**\nLawrence, Indiana.\n**(29)**\nNoblesville, Indiana.\n**(30)**\nWestfield, Indiana.\n**(31)**\nZionsville, Indiana.\n**(32)**\nCamargo, Kentucky.\n**(33)**\nLouisiana State University, Baton Rouge, Louisiana.\n**(34)**\nMontz, Louisiana.\n**(35)**\nQuartzite Township, Minnesota.\n**(36)**\nSpringwater Township, Minnesota.\n**(37)**\nGrass Valley, Nevada.\n**(38)**\nSwanzey, New Hampshire.\n**(39)**\nKinnelon, New Jersey.\n**(40)**\nFlanders, New York.\n**(41)**\nGlendale, New York.\n**(42)**\nNorthampton, New York.\n**(43)**\nPendleton, New York.\n**(44)**\nRiverside, New York.\n**(45)**\nWheatfield, New York.\n**(46)**\nHarnett County, North Carolina.\n**(47)**\nWeddington, North Carolina.\n**(48)**\nGreen, Ohio.\n**(49)**\nHochatown, Oklahoma.\n**(50)**\nNorth Enid, Oklahoma.\n**(51)**\nGoose Creek, South Carolina.\n**(52)**\nMauldin, South Carolina.\n**(53)**\nFairview, Texas.\n**(54)**\nFate, Texas.\n**(55)**\nHeath, Texas.\n**(56)**\nJosephine, Texas.\n**(57)**\nMurphy, Texas.\n**(58)**\nNorthlake, Texas.\n**(59)**\nParker, Texas.\n**(60)**\nSargent, Texas.\n**(61)**\nFairlawn, Virginia.\n**(62)**\nCaledonia, Wisconsin.\n**(63)**\nFranklin, Wisconsin.\n**(64)**\nGlendale, Wisconsin.\n**(65)**\nGreenfield, Wisconsin.\n**(66)**\nVillage of Harrison, Wisconsin.\n**(67)**\nVillage of Mount Pleasant, Wisconsin.\n**(68)**\nVillage of Somers, Wisconsin.\n**(69)**\nRochester, Wisconsin.",
      "versionDate": "2025-10-01",
      "versionType": "Introduced in Senate"
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-10T21:58:52Z"
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
      "date": "2025-10-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2961is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the United States Postal Service to designate single, unique ZIP Codes for certain communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:17Z"
    },
    {
      "title": "A bill to direct the United States Postal Service to designate single, unique ZIP Codes for certain communities, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-02T10:56:14Z"
    }
  ]
}
```
