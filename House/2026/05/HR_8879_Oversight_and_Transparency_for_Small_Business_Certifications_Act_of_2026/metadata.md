# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8879?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8879
- Title: Oversight and Transparency for Small Business Certifications Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8879
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-21T08:07:42Z
- Update date including text: 2026-05-21T08:07:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Small Business.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported by the Yeas and Nays: 23 - 0.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Small Business.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported by the Yeas and Nays: 23 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8879",
    "number": "8879",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "O000176",
        "district": "2",
        "firstName": "Johnny",
        "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
        "lastName": "Olszewski",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Oversight and Transparency for Small Business Certifications Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:42Z",
    "updateDateIncludingText": "2026-05-21T08:07:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 23 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-19",
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
        "item": [
          {
            "date": "2026-05-20T21:43:27Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-19T16:00:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "sponsorshipDate": "2026-05-19",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8879ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8879\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2026 Mr. Olszewski (for himself and Mr. Wied ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act to require a report on small business concern participation in a covered contracting programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Oversight and Transparency for Small Business Certifications Act of 2026 .\n#### 2. Report on small business concern participation in a covered contracting programs\nSection 10(c) of the Small Business Act ( 15 U.S.C. 639(c) ) is amended to read as follows:\n(c) Certification reports (1) In general Along with the submission to Congress of the budget of the President for each fiscal year pursuant to section 1105(a) of title 31, United States Code, the Administrator shall submit a report on small business concern participation in a covered contracting program during the year covered by the report that includes the following: (A) The total number of unique small business concerns certified for participation in a covered contracting program. (B) With respect to applications of small business concerns for participation in a covered contracting program\u2014 (i) the total number of applications for participation that have sufficient information for the Administrator to issue a certification determination, disaggregated by\u2014 (I) the number of applications certified for each covered contracting program; and (II) the number of applications for which a determination has not been made for any covered contracting program; (ii) the number of applications for certification for two or more covered contracting programs and the percentage of total applicants that received two or more certifications; (iii) the number of applications received through the single, unified platform established by the Administrator for receipt of certification applications; and (iv) the number of small business concerns certified for participation in a covered contracting program for which such certification documentation is contain in a system other than the platform described in clause (iii), disaggregated by covered contracting program. (C) With respect to applications of small business concerns for certification as a small business concern owned and controlled by service-disabled veterans that have sufficient information for the Administrator to issue a certification determination\u2014 (i) the number of applications certified; (ii) the number of applications denied; and (iii) the number of applications for which a determination has not been made. (D) With respect to each application of a small business concern for certification as a small business concern owned and controlled by service-disabled veterans, the timeframe between the date of submission of a completed application and the issuance of a certification or recertification determination, disaggregated by\u2014 (i) the number, expressed as a percentage, of certification determinations made within the timeframe established by the Administration; (ii) the average time for a first-time applicant to receive a certification determination; and (iii) the average time for an applicant that is a small business concern owned and controlled by service-disabled veterans to receive a recertification determination. (E) With respect to applications of small business concerns for certification as a small business concern owned and controlled by women that have sufficient information for the Administrator to issue a certification determination\u2014 (i) the number of applications certified; (ii) of the applications described in clause (i), the number certified that are eligible for award of a sole source contract under section 8(m)(7); (iii) the number of applications certified that were processed by a national certifying entity described in section 8(m)(2)(E); (iv) the number of applications denied; and (v) the number of applications for which a determination has not been made. (F) Of the applications described in subparagraph (E)(ii), the number of such applications that initially did not include sufficient information for the Administrator to issue a certification determination. (G) With respect to each application of a small business concern for certification as a small business concern owned and controlled by women, the timeframe between the date of submission of a completed application and the issuance of a certification or recertification determination, disaggregated by\u2014 (i) the number, expressed as a percentage, of certification determinations made within the timeframe established by the Administration; (ii) the average time for a first-time applicant to receive a certification determination; (iii) the average time for an applicant that is a small business concern owned and controlled by women to receive a recertification determination; and (iv) the average time for an applicant certified by a national certifying entity to receive a determination from the Administrator, disaggregated by initial certification applications and recertification applications. (H) With respect to applications of small business concerns for certification as a qualified HUBZone small business concern that have sufficient information for the Administrator to issue a certification determination\u2014 (i) the number of applications certified; (ii) the number of applications denied; and (iii) the number of applications for which a determination has not been made. (I) With respect to each application of a small business concern for certification as a qualified HUBZone small business concern, the timeframe between the date of submission of a completed application and the issuance of a certification or recertification determination, disaggregated by\u2014 (i) the number, expressed as a percentage, of certification determinations made within the timeframe established by the Administration; (ii) the average time for a first-time applicant to receive a certification determination; and (iii) the average time for an applicant that is a qualified HUBZone small business concern to receive a recertification determination. (2) Covered contracting program defined In this subsection, the term covered contracting program means contracting assistance provided by the Administrator under following: (A) Section 8(a). (B) Section 8(m). (C) Section 31. (D) Section 36. .",
      "versionDate": "2026-05-19",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8879ih.xml"
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
      "title": "Oversight and Transparency for Small Business Certifications Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Oversight and Transparency for Small Business Certifications Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-20T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act to require a report on small business concern participation in a covered contracting programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T08:19:34Z"
    }
  ]
}
```
