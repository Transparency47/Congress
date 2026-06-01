# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2863?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2863
- Title: RRLEF Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2863
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-03-31T15:52:05Z
- Update date including text: 2026-03-31T15:52:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2863",
    "number": "2863",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "RRLEF Act of 2025",
    "type": "S",
    "updateDate": "2026-03-31T15:52:05Z",
    "updateDateIncludingText": "2026-03-31T15:52:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T16:13:17Z",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2863is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2863\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Ms. Duckworth (for herself, Mr. Durbin , Mr. Blumenthal , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 with respect to eligibility under the Edward Byrne Memorial Justice Assistance Grant Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Responsible Retirement of Law Enforcement Firearms Act of 2025 or the RRLEF Act of 2025 .\n#### 2. Eligibility under Edward Byrne Memorial Justice Assistance Grant Program\n##### (a) Certification requirement\nSection 502 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10153 ) is amended\u2014\n**(1)**\nin subsection (a)(5)\u2014\n**(A)**\nin subparagraph (C), by striking and ;\n**(B)**\nin subparagraph (D), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(E) the applicant and each grantee or subgrantee under the jurisdiction of the applicant shall not transfer a firearm to, or purchase a firearm from, a licensed dealer that is on the list of covered licensed dealers most recently published at the time of certification by the Director of the Bureau of Alcohol, Tobacco, Firearms, and Explosives under section 2(b)(2) of the RRLEF Act of 2025 . ; and\n**(2)**\nby adding at the end the following:\n(c) Definitions In this section\u2014 (1) the term covered licensed dealer means a licensed dealer with respect to whom, in not less than two of the three calendar years prior to the publication of the list under section 2(b)(2) of the RRLEF Act of 2025 , the National Tracing Center of the Bureau of Alcohol, Tobacco, Firearms, and Explosives has traced to the firearms business of such licensed dealer, in such calendar years, not less than 25 firearms that had a short time-to-crime; (2) the terms licensed dealer and firearm have the meaning given such terms in section 921(a) of title 18, United States Code; and (3) the term short time-to-crime means, a period of not more than three calendar years between the date of the last known retail sale of a firearm and the date on which a law enforcement agency recovers such firearm as a result of such firearm being purchased for, possessed during, or used in, an actual or suspected criminal offense. .\n##### (b) Public disclosure of database information of Bureau of Alcohol, Tobacco, Firearms and Explosives\nNot later than 120 days after the date of enactment of this Act, and annually thereafter, the Attorney General, acting through the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives, shall\u2014\n**(1)**\nnotify a State or local law enforcement agency if any firearm (as such term is defined in section 921(a) of title 18, United States Code) that was transferred by such agency was used, or suspected of being used, in the commission of a criminal offense, as traced by the National Tracing Center of the Bureau; and\n**(2)**\nmake publicly available on the internet website of the Bureau a list of each covered licensed dealer (as such term is defined in section 502(c) of the Omnibus Crime Control and Safe Streets Act of 1968, as added by subsection (a) of this section).\n##### (c) Repeal of certain limitations on public disclosure of database information of Bureau of Alcohol, Tobacco, Firearms and Explosives\n**(1) Public Law 112\u201355**\nThe 6th proviso in the matter under the under the heading Salaries and Expenses under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives in title II of division B of the Consolidated and Further Continuing Appropriations Act, 2012 ( 18 U.S.C. 923 note; Public Law 112\u201355 ) is amended by striking and in each fiscal year thereafter .\n**(2) Public Law 111\u2013117**\nThe 6th proviso in the matter under the heading Salaries and Expenses under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives in title II of division B of the Consolidated Appropriations Act, 2010 ( 18 U.S.C. 923 note; Public Law 111\u2013117 ) is amended by striking beginning in fiscal year 2010 and thereafter and inserting in fiscal year 2010 .\n**(3) Public Law 111\u20138**\nThe 6th proviso in the matter under the heading Salaries and Expenses under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives in title II of division B of the Omnibus Appropriations Act, 2009 ( 18 U.S.C. 923 note; Public Law 111\u20138 ) is amended by striking beginning in fiscal year 2009 and thereafter and inserting in fiscal year 2009 .\n**(4) Public Law 110\u2013161**\nThe 6th proviso in the matter under the heading Salaries and Expenses under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives in title II of division B of the Consolidated Appropriations Act, 2008 ( 18 U.S.C. 923 note; Public Law 110\u2013161 ) is amended by striking beginning in fiscal year 2008 and thereafter and inserting in fiscal year 2008 .\n**(5) Public Law 109\u2013108**\nThe 6th proviso in the matter under the heading Salaries and Expenses under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives in title I of the Science, State, Justice, Commerce, and Related Agencies Appropriations Act, 2006 ( 18 U.S.C. 923 note; Public Law 109\u2013108 ) is amended by striking with respect to any fiscal year and inserting with respect to fiscal year 2006 .\n**(6) Public Law 108\u2013447**\nThe 6th proviso in the matter under the heading Salaries and Expenses under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives in title I of division B of the Consolidated Appropriations Act, 2005 ( 18 U.S.C. 923 note; Public Law 108\u2013447 ) is amended by striking with respect to any fiscal year and inserting with respect to fiscal year 2005 .\n**(7) Public Law 108\u20137**\nSection 644 of the Departments of Commerce, Justice, and State, the Judiciary, and Related Agencies Appropriations Act, 2003 ( 5 U.S.C. 552 note; Public Law 108\u20137 ) is amended by striking with respect to any fiscal year and inserting with respect to fiscal year 2003 .",
      "versionDate": "",
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
        "actionDate": "2025-09-18",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5453",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RRLEF Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-16T18:51:27Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2863is.xml"
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
      "title": "RRLEF Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RRLEF Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Responsible Retirement of Law Enforcement Firearms Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 with respect to eligibility under the Edward Byrne Memorial Justice Assistance Grant Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:23Z"
    }
  ]
}
```
