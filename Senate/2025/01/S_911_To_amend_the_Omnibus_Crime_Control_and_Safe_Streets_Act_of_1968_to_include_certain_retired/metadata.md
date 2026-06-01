# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/911?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/911
- Title: Chief Herbert D. Proffitt Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 911
- Origin chamber: Senate
- Introduced date: 2025-03-10
- Update date: 2026-01-05T22:00:54Z
- Update date including text: 2026-01-05T22:00:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in Senate
- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 81.
- 2025-07-29 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S4796; text: CR S4797)
- 2025-07-29 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-08-01 - Floor: Message on Senate action sent to the House.
- 2025-08-01 10:02:02 - Floor: Held at the desk.
- 2025-08-01 10:02:02 - Floor: Received in the House.
- Latest action: 2025-03-10: Introduced in Senate

## Actions

- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 81.
- 2025-07-29 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S4796; text: CR S4797)
- 2025-07-29 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-08-01 - Floor: Message on Senate action sent to the House.
- 2025-08-01 10:02:02 - Floor: Held at the desk.
- 2025-08-01 10:02:02 - Floor: Received in the House.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/911",
    "number": "911",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Chief Herbert D. Proffitt Act of 2025",
    "type": "S",
    "updateDate": "2026-01-05T22:00:54Z",
    "updateDateIncludingText": "2026-01-05T22:00:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H14000",
      "actionDate": "2025-08-01",
      "actionTime": "10:02:02",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionCode": "H15000",
      "actionDate": "2025-08-01",
      "actionTime": "10:02:02",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S4796; text: CR S4797)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 81.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
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
        "item": [
          {
            "date": "2025-05-20T20:15:22Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-15T17:30:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-10T19:45:42Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "KY"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "CT"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "IA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "IL"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "AZ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "DE"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "NE"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "KS"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s911is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 911\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2025 Ms. Cortez Masto (for herself and Mr. McConnell ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to include certain retired law enforcement officers in the public safety officers\u2019 death benefits program.\n#### 1. Short title\nThis Act may be cited as the Chief Herbert D. Proffitt Act of 2025 .\n#### 2. Inclusion of certain retired public safety officers in the public safety officers\u2019 death benefits program\n##### (a) In general\nSection 1201 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281 ) is amended by adding at the end the following:\n(p) Personal injury to retired law enforcement officer (1) Definition In this subsection, the term retired law enforcement officer means an individual who separated from service in good standing as a law enforcement officer in an official capacity at a public agency with or without compensation. (2) Eligibility A retired law enforcement officer shall be eligible for a benefit under this part if the officer died or became permanently and totally disabled as the direct and proximate result of a personal injury resulting from a targeted attack because of the retired law enforcement officer\u2019s service as a law enforcement officer. .\n##### (b) Retroactive applicability\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall\u2014\n**(A)**\ntake effect on the date of enactment of this Act; and\n**(B)**\napply to any matter\u2014\n**(i)**\npending before the Bureau of Justice Assistance or otherwise on the date of enactment of this Act; or\n**(ii)**\nfiled (consistent with pre-existing effective dates) or accruing after the date of enactment of this Act.\n**(2) Exceptions**\nThe amendment made by this section shall apply to any action taken against a retired law enforcement officer described in section 1201(p) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 (as added by this Act) on or after January 1, 2012.",
      "versionDate": "2025-03-10",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s911rs.xml",
      "text": "II\nCalendar No. 81\n119th CONGRESS\n1st Session\nS. 911\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2025 Ms. Cortez Masto (for herself, Mr. McConnell , Mr. Blumenthal , Mr. Grassley , Mr. Durbin , Mr. Gallego , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 20, 2025 Reported by Mr. Grassley , without amendment\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to include certain retired law enforcement officers in the public safety officers\u2019 death benefits program.\n#### 1. Short title\nThis Act may be cited as the Chief Herbert D. Proffitt Act of 2025 .\n#### 2. Inclusion of certain retired public safety officers in the public safety officers\u2019 death benefits program\n##### (a) In general\nSection 1201 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281 ) is amended by adding at the end the following:\n(p) Personal injury to retired law enforcement officer (1) Definition In this subsection, the term retired law enforcement officer means an individual who separated from service in good standing as a law enforcement officer in an official capacity at a public agency with or without compensation. (2) Eligibility A retired law enforcement officer shall be eligible for a benefit under this part if the officer died or became permanently and totally disabled as the direct and proximate result of a personal injury resulting from a targeted attack because of the retired law enforcement officer\u2019s service as a law enforcement officer. .\n##### (b) Retroactive applicability\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall\u2014\n**(A)**\ntake effect on the date of enactment of this Act; and\n**(B)**\napply to any matter\u2014\n**(i)**\npending before the Bureau of Justice Assistance or otherwise on the date of enactment of this Act; or\n**(ii)**\nfiled (consistent with pre-existing effective dates) or accruing after the date of enactment of this Act.\n**(2) Exceptions**\nThe amendment made by this section shall apply to any action taken against a retired law enforcement officer described in section 1201(p) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 (as added by this Act) on or after January 1, 2012.",
      "versionDate": "2025-05-20",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s911es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 911\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to include certain retired law enforcement officers in the public safety officers\u2019 death benefits program.\n#### 1. Short title\nThis Act may be cited as the Chief Herbert D. Proffitt Act of 2025 .\n#### 2. Inclusion of certain retired public safety officers in the public safety officers\u2019 death benefits program\n##### (a) In general\nSection 1201 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281 ) is amended by adding at the end the following:\n(p) Personal injury to retired law enforcement officer (1) Definition In this subsection, the term retired law enforcement officer means an individual who separated from service in good standing as a law enforcement officer in an official capacity at a public agency with or without compensation. (2) Eligibility A retired law enforcement officer shall be eligible for a benefit under this part if the officer died or became permanently and totally disabled as the direct and proximate result of a personal injury resulting from a targeted attack because of the retired law enforcement officer\u2019s service as a law enforcement officer. .\n##### (b) Retroactive applicability\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall\u2014\n**(A)**\ntake effect on the date of enactment of this Act; and\n**(B)**\napply to any matter\u2014\n**(i)**\npending before the Bureau of Justice Assistance or otherwise on the date of enactment of this Act; or\n**(ii)**\nfiled (consistent with pre-existing effective dates) or accruing after the date of enactment of this Act.\n**(2) Exceptions**\nThe amendment made by this section shall apply to any action taken against a retired law enforcement officer described in section 1201(p) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 (as added by this Act) on or after January 1, 2012.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-12",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1236",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Chief Herbert D. Proffitt Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2025-06-02T20:31:32Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-02T20:31:27Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-06-02T20:31:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-28T12:43:51Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s911is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s911rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s911es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Chief Herbert D. Proffitt Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T11:03:18Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Chief Herbert D. Proffitt Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Chief Herbert D. Proffitt Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-22T02:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Chief Herbert D. Proffitt Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to include certain retired law enforcement officers in the public safety officers' death benefits program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:54Z"
    }
  ]
}
```
