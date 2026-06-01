# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4505?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4505
- Title: A bill to require the United States Postal Service to designate ZIP Codes for certain communities.
- Congress: 119
- Bill type: S
- Bill number: 4505
- Origin chamber: Senate
- Introduced date: 2026-05-12
- Update date: 2026-05-20T10:56:39Z
- Update date including text: 2026-05-20T10:56:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in Senate
- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-05-12: Introduced in Senate

## Actions

- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4505",
    "number": "4505",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "A bill to require the United States Postal Service to designate ZIP Codes for certain communities.",
    "type": "S",
    "updateDate": "2026-05-20T10:56:39Z",
    "updateDateIncludingText": "2026-05-20T10:56:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-12",
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
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T22:19:37Z",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "WY"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CO"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "FL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4505is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4505\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2026 Ms. Ernst (for herself, Mr. Padilla , Mr. Barrasso , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the United States Postal Service to designate ZIP Codes for certain communities.\n#### 1. Designation of ZIP Codes\nNot later than 1 year after the date of enactment of this Act, the United States Postal Service shall designate a single, unique ZIP Code for each of the following communities:\n**(1)**\nCanyon Lake, California.\n**(2)**\nEastvale, California.\n**(3)**\nHidden Hills, California.\n**(4)**\nIndustry, California.\n**(5)**\nIrwindale, California.\n**(6)**\nNorth Tustin, California.\n**(7)**\nRossmoor, California.\n**(8)**\nSan Pablo, California.\n**(9)**\nTehachapi, California.\n**(10)**\nTorrance, California.\n**(11)**\nCastle Pines, Colorado.\n**(12)**\nCentennial, Colorado.\n**(13)**\nCherry Hills Village, Colorado.\n**(14)**\nFrederick, Colorado.\n**(15)**\nGreenwood Village, Colorado.\n**(16)**\nHighlands Ranch, Colorado.\n**(17)**\nKeystone, Colorado.\n**(18)**\nLone Tree, Colorado.\n**(19)**\nMountain Village, Colorado.\n**(20)**\nMt. Crested Butte, Colorado.\n**(21)**\nSeverance, Colorado.\n**(22)**\nSilver Cliff, Colorado.\n**(23)**\nSterling Ranch, Colorado.\n**(24)**\nSuperior, Colorado.\n**(25)**\nTelluride, Colorado.\n**(26)**\nScotland, Connecticut.\n**(27)**\nCoconut Creek, Florida.\n**(28)**\nCooper City, Florida.\n**(29)**\nDeerfield Beach, Florida.\n**(30)**\nFort Myers, Florida.\n**(31)**\nLighthouse Point, Florida.\n**(32)**\nMiami Lakes, Florida.\n**(33)**\nOakland Park, Florida.\n**(34)**\nOcoee, Florida.\n**(35)**\nParkland, Florida.\n**(36)**\nVillage of Estero, Florida.\n**(37)**\nWilton Manors, Florida.\n**(38)**\nBurr Ridge, Illinois.\n**(39)**\nCarmel, Indiana.\n**(40)**\nNoblesville, Indiana.\n**(41)**\nLawrence, Indiana.\n**(42)**\nWestfield, Indiana.\n**(43)**\nZionsville, Indiana.\n**(44)**\nUrbandale, Iowa.\n**(45)**\nCamargo, Kentucky.\n**(46)**\nLouisiana State University, Baton Rouge, Louisiana.\n**(47)**\nMontz, Louisiana.\n**(48)**\nSpringwater Township, Minnesota.\n**(49)**\nQuartzite Township, Minnesota.\n**(50)**\nGrass Valley, Nevada.\n**(51)**\nSwanzey, New Hampshire.\n**(52)**\nKinnelon, New Jersey.\n**(53)**\nFlanders, New York.\n**(54)**\nGlendale, New York.\n**(55)**\nPendleton, New York.\n**(56)**\nRiverside, New York.\n**(57)**\nWheatfield, New York.\n**(58)**\nWeddington, North Carolina.\n**(59)**\nGreen, Ohio.\n**(60)**\nHochatown, Oklahoma.\n**(61)**\nNorth Enid, Oklahoma.\n**(62)**\nGoose Creek, South Carolina.\n**(63)**\nMauldin, South Carolina.\n**(64)**\nFairview, Texas.\n**(65)**\nFate, Texas.\n**(66)**\nHeath, Texas.\n**(67)**\nJosephine, Texas.\n**(68)**\nMurphy, Texas.\n**(69)**\nNorthlake, Texas.\n**(70)**\nParker, Texas.\n**(71)**\nSargent, Texas.\n**(72)**\nHighland City, Utah.\n**(73)**\nFairlawn, Virginia.\n**(74)**\nStar Valley Ranch, Wyoming.\n**(75)**\nMills, Wyoming.",
      "versionDate": "2026-05-12",
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
        "text": "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3095",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To direct the United States Postal Service to designate single, unique ZIP Codes for certain communities, and for other purposes.",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-15T18:16:07Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4505is.xml"
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
      "title": "A bill to require the United States Postal Service to designate ZIP Codes for certain communities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T17:18:37Z"
    },
    {
      "title": "A bill to require the United States Postal Service to designate ZIP Codes for certain communities.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T10:56:23Z"
    }
  ]
}
```
