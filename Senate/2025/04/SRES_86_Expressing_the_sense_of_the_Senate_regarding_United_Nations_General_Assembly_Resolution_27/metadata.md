# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/86?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/86
- Title: A resolution expressing the sense of the Senate regarding United Nations General Assembly Resolution 2758 (XXVI) and the harmful conflation of China's "One China Principle" and the United States'"One China Policy".
- Congress: 119
- Bill type: SRES
- Bill number: 86
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-12-05T22:04:17Z
- Update date including text: 2025-12-05T22:04:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1135-1136)
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 56.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1135-1136)
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 56.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/86",
    "number": "86",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "A resolution expressing the sense of the Senate regarding United Nations General Assembly Resolution 2758 (XXVI) and the harmful conflation of China's \"One China Principle\" and the United States'\"One China Policy\".",
    "type": "SRES",
    "updateDate": "2025-12-05T22:04:17Z",
    "updateDateIncludingText": "2025-12-05T22:04:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 56.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S1135-1136)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
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
            "date": "2025-04-28T20:37:57Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-27T17:55:23Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-20T19:51:44Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "NH"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "NE"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "DE"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "VA"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "IN"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "CO"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NV"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "OR"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NV"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MD"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres86is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 86\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Risch (for himself, Mrs. Shaheen , Mr. Ricketts , and Mr. Coons ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the sense of the Senate regarding United Nations General Assembly Resolution 2758 (XXVI) and the harmful conflation of China\u2019s One China Principle and the United States' One China Policy .\nThat the Senate\u2014\n**(1)**\nreaffirms that the longstanding one China policy of the United States does not affirmatively recognize the People\u2019s Republic of China\u2019s claim to control over Taiwan and its outlying islands, but rather acknowledges this position, reaffirms the interest of the United States in a peaceful resolution of cross-Strait issues, has not agreed to take any position regarding sovereignty over Taiwan , and will not exert pressure on Taiwan to enter into negotiations with the PRC ;\n**(2)**\nreaffirms that the one China policy of the United States and the similar policies of its partners are not equivalent to the One China Principle of the Chinese Communist Party;\n**(3)**\nemphasizes that United Nations General Assembly Resolution 2758 is not equivalent to, and does not endorse, the PRC\u2019s One China Principle ;\n**(4)**\nemphasizes further that Resolution 2758 does not take a position on Taiwan\u2019s ultimate political status, as explicitly recognized by PRC leaders at the time, and does not represent a United Nations consensus on Taiwan\u2019s status;\n**(5)**\nopposes China\u2019s use of the One China Principle to coerce the United States, Taiwan, and other countries to accept its claims over Taiwan;\n**(6)**\nsupports Taiwan\u2019s diplomatic allies in continuing official relationships with Taiwan, and other nations across the world in strengthening their partnerships with Taiwan;\n**(7)**\nreaffirms support for Taiwan\u2019s membership in international organizations for which statehood is not a requirement for membership and encourages meaningful participation for Taiwan in organizations in which its membership is not possible;\n**(8)**\nrecognizes that Taiwan is a reliable and indispensable partner on issues ranging from global health to advanced manufacturing, and its resources and expertise are assets from which the international community should fully benefit;\n**(9)**\nsupports ensuring that Taiwan passport holders are able to access United Nations grounds and should not be required to provide PRC-issued identification;\n**(10)**\nencourages the United States Government to work with partners on joint efforts to counter China\u2019s false narratives about Resolution 2758; and\n**(11)**\nsupports the efforts of other countries to differentiate between their policies and the One China Principle to counter China\u2019s propaganda about international views of Taiwan.",
      "versionDate": "2025-02-20",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres86rs.xml",
      "text": "III\nCalendar No. 56\n119th CONGRESS\n1st Session\nS. RES. 86\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Risch (for himself, Mrs. Shaheen , Mr. Ricketts , Mr. Coons , Mr. Scott of Florida , Ms. Duckworth , Mr. Kim , Mr. Kaine , Mr. Cornyn , Mr. Young , Mr. Bennet , Ms. Rosen , Mr. Merkley , Ms. Cortez Masto , and Mr. Van Hollen ) submitted the following resolution; which was referred to the Committee on Foreign Relations of the Senate\nApril 28, 2025 Reported by Mr. Risch , without amendment\nRESOLUTION\nExpressing the sense of the Senate regarding United Nations General Assembly Resolution 2758 (XXVI) and the harmful conflation of China\u2019s One China Principle and the United States' One China Policy .\nThat the Senate\u2014\n**(1)**\nreaffirms that the longstanding one China policy of the United States does not affirmatively recognize the People\u2019s Republic of China\u2019s claim to control over Taiwan and its outlying islands, but rather acknowledges this position, reaffirms the interest of the United States in a peaceful resolution of cross-Strait issues, has not agreed to take any position regarding sovereignty over Taiwan , and will not exert pressure on Taiwan to enter into negotiations with the PRC ;\n**(2)**\nreaffirms that the one China policy of the United States and the similar policies of its partners are not equivalent to the One China Principle of the Chinese Communist Party;\n**(3)**\nemphasizes that United Nations General Assembly Resolution 2758 is not equivalent to, and does not endorse, the PRC\u2019s One China Principle ;\n**(4)**\nemphasizes further that Resolution 2758 does not take a position on Taiwan\u2019s ultimate political status, as explicitly recognized by PRC leaders at the time, and does not represent a United Nations consensus on Taiwan\u2019s status;\n**(5)**\nopposes China\u2019s use of the One China Principle to coerce the United States, Taiwan, and other countries to accept its claims over Taiwan;\n**(6)**\nsupports Taiwan\u2019s diplomatic allies in continuing official relationships with Taiwan, and other nations across the world in strengthening their partnerships with Taiwan;\n**(7)**\nreaffirms support for Taiwan\u2019s membership in international organizations for which statehood is not a requirement for membership and encourages meaningful participation for Taiwan in organizations in which its membership is not possible;\n**(8)**\nrecognizes that Taiwan is a reliable and indispensable partner on issues ranging from global health to advanced manufacturing, and its resources and expertise are assets from which the international community should fully benefit;\n**(9)**\nsupports ensuring that Taiwan passport holders are able to access United Nations grounds and should not be required to provide PRC-issued identification;\n**(10)**\nencourages the United States Government to work with partners on joint efforts to counter China\u2019s false narratives about Resolution 2758; and\n**(11)**\nsupports the efforts of other countries to differentiate between their policies and the One China Principle to counter China\u2019s propaganda about international views of Taiwan.",
      "versionDate": "2025-04-28",
      "versionType": "RS"
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
        "actionDate": "2025-02-21",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing the sense of the House of Representatives regarding United Nations General Assembly Resolution 2758 (XXVI) and the harmful conflation of China's \"One China Principle\" and the United States \"One China Policy\".",
      "type": "HRES"
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
            "name": "Asia",
            "updateDate": "2025-05-14T13:23:55Z"
          },
          {
            "name": "China",
            "updateDate": "2025-05-14T13:23:43Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-05-14T13:24:24Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-05-14T13:24:13Z"
          },
          {
            "name": "Sovereignty, recognition, national governance and status",
            "updateDate": "2025-05-14T13:24:03Z"
          },
          {
            "name": "Taiwan",
            "updateDate": "2025-05-14T13:23:50Z"
          },
          {
            "name": "Visas and passports",
            "updateDate": "2025-05-14T13:24:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-06T15:40:34Z"
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
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres86is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres86rs.xml"
        }
      ],
      "type": "RS"
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
      "title": "A resolution expressing the sense of the Senate regarding United Nations General Assembly Resolution 2758 (XXVI) and the harmful conflation of China's \"One China Principle\" and the United States'\"One China Policy\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:25Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate regarding United Nations General Assembly Resolution 2758 (XXVI) and the harmful conflation of China's \"One China Principle\" and the United States'\"One China Policy\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T11:56:25Z"
    }
  ]
}
```
