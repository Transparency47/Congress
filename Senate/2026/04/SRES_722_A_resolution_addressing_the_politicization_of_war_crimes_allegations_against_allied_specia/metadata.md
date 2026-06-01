# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/722?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/722
- Title: A resolution addressing the politicization of war crimes allegations against allied special operations forces.
- Congress: 119
- Bill type: SRES
- Bill number: 722
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-06T20:42:25Z
- Update date including text: 2026-05-06T20:42:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2182)
- 2026-04-30 - IntroReferral: Submitted in Senate
- Latest action: 2026-04-30: Submitted in Senate

## Actions

- 2026-04-30 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2182)
- 2026-04-30 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/722",
    "number": "722",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "A resolution addressing the politicization of war crimes allegations against allied special operations forces.",
    "type": "SRES",
    "updateDate": "2026-05-06T20:42:25Z",
    "updateDateIncludingText": "2026-05-06T20:42:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S2182)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-30",
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
      "text": "Submitted in Senate",
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
          "date": "2026-04-30T19:56:51Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres722is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 722\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Ms. Ernst (for herself and Mr. Sheehy ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nAddressing the politicization of war crimes allegations against allied special operations forces.\nThat it is the sense of Congress that\u2014\n**(1)**\nthe United States profoundly appreciates and acknowledges the longstanding alliances with countries such as the United Kingdom, Australia, and other partner nations, and honors the service and sacrifices of their Armed Forces who have fought alongside United States troops in Afghanistan, Iraq, and other missions, and these sacrifices are exemplified by the lives lost and injuries suffered by allied servicemembers in these conflicts;\n**(2)**\nallied forces participated in these collective security and counterterrorism operations at the behest of and in support of mutual defense agreements and United States-led missions, and their contributions were integral to the success of those missions, reflecting a shared commitment to global security;\n**(3)**\nCongress expresses concern that retrospective, politically motivated accusations of war crimes against the special operations forces of United States allies, particularly when raised or revisited long after the fact, risk undermining the mutual trust, interoperability, and morale that underpin the United States-allied military relationships, and such accusations, if driven by political pressures rather than purely by facts and evidence, are viewed as detrimental to alliance unity and the confidence of our servicemembers;\n**(4)**\nthe executive branch, including the Department of Defense and the Department of State, is urged to work proactively with the governments of allied nations, such as Australia, the United Kingdom, and others, to ensure that any investigations or legal processes regarding alleged war crimes by their servicemembers are conducted without politicization, thereby bolstering confidence in the outcomes and reinforcing our mutual trust; and\n**(5)**\nhonoring the sacrifices of allied servicemembers and preserving the strength and cohesion of our alliances is in the national interest of the United States, and while the rule of law must always be respected, the politicization of war crimes allegations for short-term political purposes is strongly discouraged as it runs counter to our shared values and threatens to weaken the crucial alliances that safeguard international peace and security.",
      "versionDate": "2026-04-30",
      "versionType": "IS"
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
        "actionDate": "2026-04-29",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "1230",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Addressing the politicization of war crimes allegations against allied Special Operations Forces.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-05-06T20:42:25Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres722is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution addressing the politicization of war crimes allegations against allied special operations forces.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T05:18:27Z"
    },
    {
      "title": "A resolution addressing the politicization of war crimes allegations against allied special operations forces.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T10:56:35Z"
    }
  ]
}
```
