# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1913?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1913
- Title: Ending Qualified Immunity Act
- Congress: 119
- Bill type: S
- Bill number: 1913
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-12-05T21:49:05Z
- Update date including text: 2025-12-05T21:49:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1913",
    "number": "1913",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Ending Qualified Immunity Act",
    "type": "S",
    "updateDate": "2025-12-05T21:49:05Z",
    "updateDateIncludingText": "2025-12-05T21:49:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T19:58:46Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-05-22",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1913is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1913\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Markey (for himself, Ms. Warren , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Revised Statutes to remove the defense of qualified immunity in the case of any action under section 1979, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ending Qualified Immunity Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCongress passed the Act of April 20, 1871 (commonly known as the Ku Klux Klan Act ; 17 Stat. 13, chapter 22) to enforce the 14th Amendment to the Constitution of the United States and combat rampant violations of civil and constitutionally secured rights across the United States, particularly those of newly freed slaves and other Black people in the post-Civil War South.\n**(2)**\nIncluded in that Act was a provision, now codified at section 1979 of the Revised Statues (in this section referred to as section 1983 ), which provides a cause of action for individuals to file lawsuits against persons acting under color of law, including State and local officials, who violate their Federal legal and constitutionally secured rights.\n**(3)**\nUnder section 1983 a person may be held liable for acting under color of State law, even if they are not acting in accordance with State law.\n**(4)**\nSection 1983 has never included a defense or immunity for government officials who act in good faith when violating rights, nor has it ever had a defense or immunity based on whether the right was clearly established at the time of the violation.\n**(5)**\nFrom 1871 through the 1960s, government actors were not afforded qualified immunity for violating rights.\n**(6)**\nThe Supreme Court of the United States in Pierson v. Ray, 386 U.S. 547 (1967), found that government actors had a good-faith defense for making arrests under unconstitutional statutes based on a common-law defense for the tort of false arrest.\n**(7)**\nThe Supreme Court of the United States later extended the good-faith defense beyond false arrests, turning it into a general good-faith defense for government officials.\n**(8)**\nFinally, in Harlow v. Fitzgerald, 457 U.S. 800 (1982), the Supreme Court of the United States found the subjective search for good faith in the government actor unnecessary, and replaced it with an objective reasonableness standard that requires that the right be clearly established at the time of the violation for the defendant to be liable.\n**(9)**\nThe doctrine of qualified immunity has severely limited the ability of many plaintiffs to recover damages under section 1983 when their rights have been violated by State and local officials.\n**(10)**\nAs a result, the intent of Congress in passing section 1983 has been frustrated, and the rights secured by the Constitution of the United States have not been appropriately protected.\n#### 3. Sense of Congress\nIt is the sense of Congress that Congress must correct the erroneous interpretation of section 1979 of the Revised Statutes that provides for qualified immunity and reiterate the standard found on the face of the statute, which does not limit liability on the basis of the good-faith belief of the defendant or on the basis that the right was not clearly established at the time of the violation.\n#### 4. Removal of qualified immunity\nSection 1979 of the Revised Statutes ( 42 U.S.C. 1983 ) is amended\u2014\n**(1)**\nby inserting (a) before Every person ; and\n**(2)**\nby adding at the end the following:\n(b) It shall not be a defense to any action pending on, or filed after, the date of enactment of this subsection that, at the time of the deprivation\u2014 (1) the defendant was acting in good faith; (2) the defendant believed, reasonably or otherwise, that his or her conduct was lawful; (3) the rights, privileges, or immunities secured by the Constitution and laws were not clearly established; or (4) the state of the law was such that the defendant could not reasonably have been expected to know whether his or her conduct was lawful. .",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-05-23",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3602",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ending Qualified Immunity Act",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-06-13T12:52:15Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1913is.xml"
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
      "title": "Ending Qualified Immunity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ending Qualified Immunity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Revised Statutes to remove the defense of qualified immunity in the case of any action under section 1979, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:29Z"
    }
  ]
}
```
