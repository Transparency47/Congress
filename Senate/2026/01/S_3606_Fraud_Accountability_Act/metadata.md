# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3606?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3606
- Title: Fraud Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 3606
- Origin chamber: Senate
- Introduced date: 2026-01-08
- Update date: 2026-03-05T12:03:20Z
- Update date including text: 2026-03-05T12:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in Senate
- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-01-08: Introduced in Senate

## Actions

- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3606",
    "number": "3606",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Fraud Accountability Act",
    "type": "S",
    "updateDate": "2026-03-05T12:03:20Z",
    "updateDateIncludingText": "2026-03-05T12:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T19:54:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "TX"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "AR"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "NC"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "ND"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "SC"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "TN"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "IN"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "OK"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "OH"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "MT"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "MT"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "KS"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "WY"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NE"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3606is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3606\nIN THE SENATE OF THE UNITED STATES\nJanuary 8 (legislative day, January 7), 2026 Mrs. Blackburn (for herself, Mr. Cornyn , Mr. Cotton , Mr. Budd , Mr. Cramer , Mr. Graham , and Mr. Hagerty ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo subject aliens convicted of fraud to deportation and to bestow concurrent jurisdiction to revoke the citizenship of any naturalized United States citizen convicted of fraud on any court that enters such a conviction.\n#### 1. Short title\nThis Act may be cited as the Fraud Accountability Act .\n#### 2. Including fraud as a deportable offense\nSection 237(a)(2)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2)(A) ) is amended\u2014\n**(1)**\nby redesignating clause (vi) as clause (vii);\n**(2)**\nby inserting after clause (v) the following:\n(vi) Notwithstanding the fraud loss threshold established in the definition of aggravated felony under section 101(a)(43)(M), any alien who is convicted of a crime involving fraud committed against any private individual, fund, corporation, or government entity is deportable. ; and\n**(3)**\nin clause (vii), as redesignated, by striking and (iv) and inserting (iv), and (vi) .\n#### 3. Mandatory detention\nSection 236(c)(1)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1227(c)(1)(B) ) is amended by striking covered in section 237(a)(2)(A)(ii), (A)(iii), (B), (C), or (D) and inserting described in subparagraph (A)(ii), (A)(iii), (A)(vi), (B), (C), or (D) of section 237(a)(2); .\n#### 4. Denaturalization for fraud and other criminal offenses\nSection 340 of the Immigration and Nationality Act ( 8 U.S.C. 1451 ) is amended\u2014\n**(1)**\nby redesignating subsections (f), (g), and (h) as subsections (g), (h), and (i), respectively; and\n**(2)**\nby inserting after subsection (e) the following:\n(f) (1) At the time any court in the United States enters a conviction of any naturalized United States citizen for a criminal offense described in section 237(a)(2), such court shall\u2014 (A) revoke, set aside, and declare void the final order admitting such person to citizenship; and (B) declare the certificate of naturalization of such person to be canceled. (2) Notwithstanding section 1331 of title 28, United States Code, any court referred to in paragraph (1) shall have jurisdiction to take the actions described in subparagraphs (A) and (B) of such paragraph with respect to a person described in such paragraph. .\n#### 5. Effective date; applicability\n##### (a) Effective date\nThis Act and the amendments made by this Act shall take effect on the date of the enactment of this Act.\n##### (b) Applicability\nThe amendments made by section 4 shall apply to any conduct by any alien constituting fraud that was committed on or after September 30, 1996, against any private individual, fund, corporation, or government entity for which such alien was not arrested, charged, or indicted before the date of the enactment of this Act.",
      "versionDate": "2026-01-08",
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
        "actionDate": "2026-01-08",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6975",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fraud Accountability Act",
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
        "name": "Immigration",
        "updateDate": "2026-01-26T13:46:53Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3606is.xml"
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
      "title": "Fraud Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fraud Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to subject aliens convicted of fraud to deportation and to bestow concurrent jurisdiction to revoke the citizenship of any naturalized United States citizen convicted of fraud on any court that enters such a conviction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T03:48:28Z"
    }
  ]
}
```
