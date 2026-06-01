# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6975?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6975
- Title: Fraud Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 6975
- Origin chamber: House
- Introduced date: 2026-01-08
- Update date: 2026-01-26T13:47:17Z
- Update date including text: 2026-01-26T13:47:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-08: Introduced in House

## Actions

- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6975",
    "number": "6975",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Fraud Accountability Act",
    "type": "HR",
    "updateDate": "2026-01-26T13:47:17Z",
    "updateDateIncludingText": "2026-01-26T13:47:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-08",
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
      "actionDate": "2026-01-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T15:00:15Z",
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
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "WI"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "PA"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6975ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6975\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 8, 2026 Mr. Carter of Georgia (for himself, Mr. Wied , and Mr. Kelly of Pennsylvania ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo subject aliens convicted of fraud to deportation and to bestow concurrent jurisdiction to revoke the citizenship of any naturalized United States citizen convicted of fraud on any court that enters such a conviction.\n#### 1. Short title\nThis Act may be cited as the Fraud Accountability Act .\n#### 2. Including fraud as a deportable offense\nSection 237(a)(2)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2)(A) ) is amended\u2014\n**(1)**\nby redesignating clause (vi) as clause (vii);\n**(2)**\nby inserting after clause (v) the following:\n(vi) Notwithstanding the fraud loss threshold established in the definition of aggravated felony under section 101(a)(43)(M), any alien who is convicted of a crime involving fraud committed against any private individual, fund, corporation, or government entity is deportable. ; and\n**(3)**\nin clause (vii), as redesignated, by striking and (iv) and inserting (iv), and (vi) .\n#### 3. Mandatory detention\nSection 236(c)(1)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1227(c)(1)(B) ) is amended by striking covered in section 237(a)(2)(A)(ii), (A)(iii), (B), (C), or (D) and inserting described in subparagraph (A)(ii), (A)(iii), (A)(vi), (B), (C), or (D) of section 237(a)(2); .\n#### 4. Denaturalization for fraud and other criminal offenses\nSection 340 of the Immigration and Nationality Act ( 8 U.S.C. 1451 ) is amended\u2014\n**(1)**\nby redesignating subsections (f), (g), and (h) as subsections (g), (h), and (i), respectively; and\n**(2)**\nby inserting after subsection (e) the following:\n(f) (1) At the time any court in the United States enters a conviction of any naturalized United States citizen for a criminal offense described in section 237(a)(2), such court shall\u2014 (A) revoke, set aside, and declare void the final order admitting such person to citizenship; and (B) declare the certificate of naturalization of such person to be canceled. (2) Notwithstanding section 1331 of title 28, United States Code, any court referred to in paragraph (1) shall have jurisdiction to take the actions described in subparagraphs (A) and (B) of such paragraph with respect to a person described in such paragraph. .\n#### 5. Effective date; applicability\n##### (a) Effective date\nThis Act and the amendments made by this Act shall take effect on the date of the enactment of this Act.\n##### (b) Applicability\nThe amendments made by section 4 shall apply to any conduct by any alien constituting fraud that was committed on or after September 30, 1996, against any private individual, fund, corporation, or government entity for which such alien was not arrested, charged, or indicted before the date of the enactment of this Act.",
      "versionDate": "2026-01-08",
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
        "actionDate": "2026-01-08",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3606",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fraud Accountability Act",
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
        "name": "Immigration",
        "updateDate": "2026-01-26T13:47:17Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6975ih.xml"
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
      "title": "Fraud Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T07:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fraud Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T07:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To subject aliens convicted of fraud to deportation and to bestow concurrent jurisdiction to revoke the citizenship of any naturalized United States citizen convicted of fraud on any court that enters such a conviction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T05:33:35Z"
    }
  ]
}
```
