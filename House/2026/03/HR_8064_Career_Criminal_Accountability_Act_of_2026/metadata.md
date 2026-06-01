# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8064?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8064
- Title: Career Criminal Accountability Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8064
- Origin chamber: House
- Introduced date: 2026-03-24
- Update date: 2026-04-28T08:06:29Z
- Update date including text: 2026-04-28T08:06:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-24: Introduced in House

## Actions

- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8064",
    "number": "8064",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Career Criminal Accountability Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:29Z",
    "updateDateIncludingText": "2026-04-28T08:06:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
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
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:01:05Z",
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
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "TX"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8064ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8064\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2026 Mr. Roy introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to provide for sentencing of three strikes offenders.\n#### 1. Short title\nThis Act may be cited as the Career Criminal Accountability Act of 2026 .\n#### 2. Imposition of a sentence\nSection 3553(a) of title 18, United States Code, is amended by striking The court shall impose and inserting Except as otherwise provided in section 3559A, the court shall impose .\n#### 3. Three strikes offenders\nSubchapter A of chapter 227 of title 18, United States Code, is amended\u2014\n**(1)**\nby adding at the end the following:\n3559A. Three strikes offenders (a) In general In determining the appropriate sentence for a defendant, the sentencing judge shall determine whether the defendant is required to be sentenced as a three-strikes offender, as defined in subsection (b), and shall sentence said defendant in accordance with this section. (b) Strike counts In determining whether the defendant is required to be sentenced as a three-strikes offender, the court shall determine the number of strikes accrued by the defendant according to the following: (1) Any conviction for a strike-eligible misdemeanor, set forth in subparagraphs (A) through (C) of subsection (e)(2), shall count as one-quarter (\u00bc) strike. (2) Any conviction for a strike-eligible nonviolent felony, set forth in subparagraphs (D) through (T) of subsection (e)(2), shall count as one-half (\u00bd) strike. (3) Any conviction for a strike-eligible firearm-related felony, set forth in subparagraphs (U) through (FF) of subsection (e)(2), shall count as one (1) strike. (4) Any conviction for a strike-eligible violent felony, set forth in subparagraphs (GG) through (JJJ) of subsection (e)(2), shall count as one (1) strike. (5) A defendant shall not accrue any strikes for any misdemeanor convictions for offenses committed while the defendant was a juvenile. (6) Any convictions for strike-eligible nonviolent or firearm-related felony offenses in cases in which the defendant was a juvenile shall result in the accrual of only one-quarter (\u00bc) strike. (7) Any convictions for strike-eligible violent felony offenses in cases in which the defendant was a juvenile shall result in the accrual of only one-half (\u00bd) strike. (c) Enhanced sentences A three-strikes offender shall\u2014 (1) have a consecutive sentence of 10 years imprisonment added to the sentence for the offenses of which the defendant was convicted if the most serious underlying offense in the instant case is a nonviolent felony set forth in subparagaphs (D) through (T) of subsection (e)(2); (2) have a consecutive sentence of 15 years imprisonment added to the sentence for the offenses of which the defendant was convicted if the most serious underlying strike-eligible offense in the instant case is a firearm-related felony set forth in subparagraphs (U) through (FF) of subsection (e)(2); and (3) have a consecutive sentence of life imprisonment added to the sentence for the offenses of which the defendant was convicted if\u2014 (A) the most serious underlying offense in the instant case is a violent felony set forth in subparagraphs (GG) through (JJJ) of subsection (e)(2); (B) the defendant has been convicted of strike-eligible offenses on at least two prior occasions; (C) at least three of the defendant\u2019s strikes stem from convictions for strike-eligible felony offenses; and (D) a 20-year consecutive sentence added if the most serious underlying offense in the instant case is a violent felony set forth in subparagraphs (X) through (VV) of subsection (e)(2), and the defendant has been convicted of strike-eligible offenses on at least two prior occasions, but fewer than three of the defendant\u2019s strikes stem from convictions for strike-eligible felony offenses. (d) Prohibition on Misdemeanor-Triggered Enhancements A defendant who reaches or surpasses the three-strikes threshold due to an instant conviction of a strike-eligible misdemeanor shall not be eligible for a sentencing enhancement under this section until said defendant is subsequently convicted of a felony, such that no sentencing enhancement shall be applied to sentences for misdemeanor convictions. (e) Definitions For purposes of this section: (1) Three-Strikes Offender The term three-strikes offender means a defendant if\u2014 (A) the instant strike-eligible offense of which the defendant is convicted constitutes an offense set forth in subparagraphs (D) through (JJJ) of paragraph (2); and (B) the defendant has, inclusive of the conviction for the instant offense and accounting for desistance credits, accrued three (3) or more strikes through prior convictions. A defendant may not be deemed a three-strikes offender if all the defendant\u2019s strikes are the result of convictions in one or more cases stemming from a single episode of criminal action. If all the defendant\u2019s strikes are the result of convictions stemming from two episodes of criminal action, each episode must include at least one (1) strike-eligible felony conviction for the defendant to be deemed a three-strikes offender. (2) Strike-Eligible Offenses The term strike eligible offense means any of the following (and includes, with regard to each offense, any attempt or conspiracy to commit the offense): (A) Section 404 of the Controlled Substances Act ( 21 U.S.C. 844 ). (B) Section 873 of title 18, United States Code. (C) Any State-level misdemeanor unlawful possession of a firearm offense. (D) Section 521 of title 18, United States Code. (E) Section 371 of title 18, United States Code. (F) Section 1956 of title 18, United States Code. (G) Section 1341 of title 18, United States Code. (H) Section 1951 of title 18, United States Code. (I) Section 1952 of title 18, United States Code. (J) Section 401(a)(1) of the Controlled Substances Act ( 21 U.S.C. 841(a)(1) ). (K) Section 406 of the Controlled Substances Act ( 21 U.S.C. 846 ). (L) Section 408 of the Controlled Substances Act ( 21 U.S.C. 848 ). (M) Section 2285 of title 18, United States Code. (N) Section 1010(a) of the Controlled Substances Import and Export Act ( 21 U.S.C. 960(a) ). (O) Section 274 of the Immigration and Nationality Act ( 8 U.S.C. 1324 ). (P) Section 278 of the Immigration and Nationality Act ( 8 U.S.C. 1328 ). (Q) Any State-level burglary offense. (R) Any State-level extortion charge. (S) Any State-level drug trafficking/distribution/possession with intent to deliver offense. (T) Section 922(d) of title 18, United States Code. (U) Section 922(g) of title 18, United States Code. (V) Section 922(j) of title 18, United States Code. (W) Section 922(k) of title 18, United States Code. (X) Section 922(n) of title 18, United States Code. (Y) Section 922(u) of title 18, United States Code. (Z) Section 922(x) of title 18, United States Code. (AA) Section 924(c) of title 18, United States Code. (BB) Section 924(n) of title 18, United States Code. (CC) Section 933(a) of title 18, United States Code. (DD) Section 2118(c)(1) of title 18, United States Code. (EE) Any State-level felon in possession of a firearm offense. (FF) Any State-level firearms trafficking offense. (GG) Section 1111 of title 18, United States Code. (HH) Section 1961 of title 18, United States Code. (II) Section 2119 of title 18, United States Code. (JJ) Section 11(b) of title 18, United States Code. (KK) Section 36(a) of title 18, United States Code. (LL) Section 111(a) of title 18, United States Code. (MM) Section 1958 of title 18, United States Code. (NN) Section 2113(d) of title 18, United States Code. (OO) Section 2118 of title 18, United States Code. (PP) Section 1581(a) of title 18, United States Code. (QQ) Section 1584 of title 18, United States Code. (RR) Section 1589 of title 18, United States Code. (SS) Section 1590 of title 18, United States Code. (TT) Section 1591 of title 18, United States Code. (UU) Section 1959 of title 18, United States Code. (VV) Section 2422(b) of title 18, United States Code. (WW) Section 2423 of title 18, United States Code. (XX) Section 2251 of title 18, United States Code. (YY) Section 2252A of title 18, United States Code. (ZZ) Section 2260 of title 18, United States Code. (AAA) Any State-level first- and second-degree murder offenses. (BBB) Any State-level sexual assault or rape offenses. (CCC) Any State-level child molestation offense. (DDD) Any State-level robbery and aggravated/armed robbery offense. (EEE) Any assault with a deadly weapon offense. (FFF) Section 1201 of title 18, United States Code. (GGG) Section 1512 of title 18, United States Code. (HHH) Section 1513 of title 18, United States Code. (III) Any State-level carjacking offenses. (JJJ) Any State-level assault on a police officer offense. (3) Single Episode of Criminal Action The term single episode of criminal action means an event or continuous series of events related to the furtherance of a single criminal act, excluding the defendant\u2019s violent resistance of any law-enforcement officer or citizens acting lawfully in defense of themselves or another that proximately causes death or serious bodily harm to the officer, citizen, or any other person. ; and\n**(2)**\nin the table of sections, by adding at the end the following:\n3559A. Three strike offenders. .",
      "versionDate": "2026-03-24",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-13T19:29:21Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8064ih.xml"
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
      "title": "Career Criminal Accountability Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Career Criminal Accountability Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to provide for sentencing of three strikes offenders.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:33Z"
    }
  ]
}
```
