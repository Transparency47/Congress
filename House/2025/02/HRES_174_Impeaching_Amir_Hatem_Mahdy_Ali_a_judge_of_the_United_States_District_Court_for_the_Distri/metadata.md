# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/174?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/174
- Title: Impeaching Amir Hatem Mahdy Ali, a judge of the United States District Court for the District of Columbia, for high crimes and misdemeanors.
- Congress: 119
- Bill type: HRES
- Bill number: 174
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-05-06T16:00:51Z
- Update date including text: 2025-05-06T16:00:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-02-27 - Committee: Submitted in House
- Latest action: 2025-02-27: Submitted in House

## Actions

- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-02-27 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/174",
    "number": "174",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Impeaching Amir Hatem Mahdy Ali, a judge of the United States District Court for the District of Columbia, for high crimes and misdemeanors.",
    "type": "HRES",
    "updateDate": "2025-05-06T16:00:51Z",
    "updateDateIncludingText": "2025-05-06T16:00:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "actionCode": "H12100",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-27T14:14:45Z",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres174ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 174\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Ogles (for himself and Mr. Gill of Texas ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nImpeaching Amir Hatem Mahdy Ali, a judge of the United States District Court for the District of Columbia, for high crimes and misdemeanors.\nThat Amir Hatem Mahdy Ali, a judge of the United States District Court for the District of Columbia, is impeached for high crimes and misdemeanors, and that the following article of impeachment be exhibited to the Senate:\nArticle of impeachment exhibited by the House of Representatives of the United States of America in the name of itself and of the people of the United States of America, against Amir Hatem Mahdy Ali, a judge of the United States District Court for the District of Columbia, in maintenance and support of its impeachment against him for high crimes and misdemeanors.\n#### Article I\nAmir Hatem Mahdy Ali, a judge of the United States District Court for the District of Columbia, engaged in a pattern of conduct that is incompatible with the trust and confidence placed in him as a Federal judge, as follows:\nJudge Ali, in a 2024 written statement to the Senate Judiciary Committee, asserted that a judge must decide issues based on an impartial and objective application of the law to the record before the court . In issuing a temporary restraining order against the pausing of funds promulgated in Executive Order 14169, Judge Ali has without merit marginalized the President\u2019s Article II authority, which vests the power to conduct foreign policy in the President of the United States, and has further compromised the President\u2019s fiduciary obligation to review federal agencies and programs. This patent violation of Constitutional precedent\u2014which necessarily precludes an explanation based on ignorance of the supreme law of the land\u2014is entirely inconsistent with serving the United States as a district court judge.\nJudge Ali, in mandating the immediate outlay of funds in contradiction of subsection (a) of Section 3 of Executive Order 14169, has done so in a manner that is arbitrary and capricious. The understood purpose of the President\u2019s Executive order was to review such funds for consistency with United States foreign policy. By mandating immediate funding disbursement of funds paused by the President\u2019s Executive order, Judge Ali did so with no consideration for the troubled history of foreign assistance through the United States Agency for International Development (USAID). A March 2021 GAO report indicates that from FY2015 until FY2019, USAID did not consistently ensure that subawards provided for projects in the Gaza Strip and Judea and Samaria complied with regulations aimed at preventing financial support for terrorism. More recently, in November 2024, USAID was found to have financed hundreds of thousands of meals for al-Qaida affiliated fighters in Syria. While arguing that the Trump administration funding pause caused irreparable harm , Judge Ali failed to consider that his decision could easily inflict irreparable harm on Americans and American interests.\nAccordingly, Judge Amir Hatem Mahdy Ali has engaged in conduct so utterly lacking in intellectual honesty and basic integrity that he is guilty of high crimes and misdemeanors, is unfit to hold the office of Federal judge, and should be removed from office.",
      "versionDate": "2025-02-27",
      "versionType": "IH"
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
        "name": "Law",
        "updateDate": "2025-05-06T16:00:51Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres174ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Impeaching Amir Hatem Mahdy Ali, a judge of the United States District Court for the District of Columbia, for high crimes and misdemeanors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T09:18:29Z"
    },
    {
      "title": "Impeaching Amir Hatem Mahdy Ali, a judge of the United States District Court for the District of Columbia, for high crimes and misdemeanors.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T09:06:19Z"
    }
  ]
}
```
