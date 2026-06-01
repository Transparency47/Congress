# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3193?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3193
- Title: Algorithm Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 3193
- Origin chamber: Senate
- Introduced date: 2025-11-18
- Update date: 2025-12-05T22:55:25Z
- Update date including text: 2025-12-05T22:55:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in Senate
- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-11-18: Introduced in Senate

## Actions

- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3193",
    "number": "3193",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Algorithm Accountability Act",
    "type": "S",
    "updateDate": "2025-12-05T22:55:25Z",
    "updateDateIncludingText": "2025-12-05T22:55:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T22:53:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3193is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3193\nIN THE SENATE OF THE UNITED STATES\nNovember 18, 2025 Mr. Curtis (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend section 230 of the Communications Act of 1934 to limit liability protection under that section for certain social media platforms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Algorithm Accountability Act .\n#### 2. Limitation of liability protection for certain social media platforms\n##### (a) In general\nSection 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ) is amended\u2014\n**(1)**\nby redesignating subsection (f) as subsection (g); and\n**(2)**\nby inserting after subsection (e) the following:\n(f) Algorithmic product design accountability (1) Duty of care in algorithmic design (A) In general A provider of a social media platform shall exercise reasonable care in the design, training, testing, deployment, operation, and maintenance of a recommendation-based algorithm on the social media platform to prevent bodily injury or death described in subparagraph (B) that a reasonable and prudent person would agree was\u2014 (i) reasonably foreseeable by the provider; and (ii) attributable, in whole or in part, to the design characteristics or performance of the recommendation-based algorithm. (B) Covered bodily injury or death Bodily injury or death described in this subparagraph, with respect to a social media platform, is bodily injury to or the death of a user of the social media platform, or bodily injury or death inflicted by a user of the social media platform upon another person, that arises from the operation of the recommendation-based algorithm. (C) Exception (i) In general Subparagraph (A) shall not apply to the ranking, ordering, promotion, recommendation, amplification, or similar curation of content that is effectuated\u2014 (I) by sorting information chronologically or reverse chronologically; or (II) to respond to an individual search for content on the social media platform initiated by a user. (ii) Exception limited to initial search Nothing in clause (i)(II) shall be construed to limit the applicability of subparagraph (A) to a provider of a social media platform, with respect to the activities of a recommendation-based algorithm, after a user of the social media platform navigates beyond the initially populated search results. (D) First Amendment protections Nothing in subparagraph (A) shall be construed to authorize the Commission to enforce that subparagraph based on the viewpoint of a user of a social media platform or of an information content provider expressed by or through any speech, expression, or information protected by the First Amendment to the Constitution of the United States. (2) Enforcement (A) Loss of liability protection Subsection (c)(1) shall not apply to a provider of a social media platform that violates paragraph (1)(A) of this subsection. (B) Private right of action If a person suffers bodily injury or death as the result of a violation of paragraph (1)(A) by the provider of a social media platform, and the bodily injury or death meets the requirements under clauses (i) and (ii) of that paragraph and paragraph (1)(B), the person or, in the case of a minor or disabled person who suffers a bodily injury or any person who dies, the legal representative of such a person, may bring a civil action in a district court of the United States of competent jurisdiction against the provider for compensatory and punitive damages. (3) Invalidity of predispute agreements and waivers (A) In general No predispute arbitration agreement or predispute joint-action waiver (as those terms are defined in section 401 of title 9, United States Code) shall be valid or enforceable with respect to a dispute arising under this subsection. (B) Applicability Any determination as to the scope or manner of applicability of subparagraph (A) shall be made by a court, rather than an arbitrator, without regard to whether an agreement described in that subparagraph purports to delegate such determination to an arbitrator. (4) Relationship to other laws Nothing in this subsection or any regulation promulgated thereunder shall be construed to prohibit or otherwise affect the enforcement of any Federal law or regulation or State law or regulation that is at least as protective of users of social media platforms as this subsection and the regulations promulgated thereunder. (5) Severability If any provision of this subsection or the application of such provision to any person or circumstance is held to be unconstitutional, the remainder of this subsection and the application of the provision to any other person or circumstance shall not be affected. (6) Definitions In this subsection: (A) Recommendation-based algorithm The term recommendation-based algorithm means, with respect to a user of a social media platform, a fully or partially automated system used to rank, order, promote, recommend, amplify, or similarly curate content, including other users, hashtags, or posts, based on the personal data of the user, including the preferences, interests, behavior, or characteristics of the user. (B) Social media platform The term social media platform \u2014 (i) means a for-profit interactive computer service that\u2014 (I) permits a user to establish an account or create a profile for the purpose of allowing the user to create, share, or view content through the account or profile; and (II) primarily serves as a service through which a user described in subclause (I) interacts with content; and (ii) does not include an interactive computer service\u2014 (I) that serves fewer than 1,000,000 registered users; (II) that is\u2014 (aa) an email program; (bb) an email distribution list; (cc) a wireless messaging service; or (dd) an online messaging service, the predominant or exclusive function of which is direct messaging, meaning messages are transmitted from the sender to a recipient and not posted within the interactive computer service or publicly; (III) that is a private platform or messaging service used by an entity solely to communicate with others employed by or affiliated with the entity; (IV) that is a teleconferencing or video conferencing service that allows reception and transmission of audio or video signals for real-time communication, provided that the real-time communication is initiated by using a unique link or identifier to facilitate access; or (V) that is an internet-based platform whose primary purpose is\u2014 (aa) to allow users to post product reviews, business reviews, or travel information and reviews; (bb) internet commerce, which may include providing a comment section; (cc) to allow users to stream music, audiobooks, or podcasts; or (dd) news or sports coverage. .\n##### (b) Technical and conforming amendments\n**(1) Trademark Act of 1946**\nSection 45 of the Act entitled An Act to provide for the registration and protection of trademarks used in commerce, to carry out the provisions of certain international conventions, and for other purposes , approved July 5, 1946 (commonly known as the Trademark Act of 1946 ) ( 15 U.S.C. 1127 ), is amended, in the definition relating to the term Internet , by striking section 230(f)(1) of the Communications Act of 1934 ( 47 U.S.C. 230(f)(1) ) and inserting section 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ) .\n**(2) Title 18, United States Code**\nSection 2421A of title 18, United States Code, is amended\u2014\n**(A)**\nin subsection (a), by striking (as such term is defined in defined in section 230(f) the Communications Act of 1934 ( 47 U.S.C. 230(f) )) and inserting (as that term is defined in section 230 of the Communications Act of 1934 ( 47 U.S.C. 230 )) ; and\n**(B)**\nin subsection (b), by striking (as such term is defined in defined in section 230(f) the Communications Act of 1934 ( 47 U.S.C. 230(f) )) and inserting (as that term is defined in section 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ) .\n**(3) Webb-Kenyon Act**\nSection 3(b)(1) of the Act entitled An Act divesting intoxicating liquors of their interstate character in certain cases , approved March 1, 1913 (commonly known as the Webb-Kenyon Act ) ( 27 U.S.C. 122b(b)(1) ), is amended by striking (as defined in section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ) and inserting (as defined in section 230 of the Communications Act of 1934 ( 47 U.S.C. 230 )) .\n**(4) Title 31, United States Code**\nSection 5362(6) of title 31, United States Code, is amended by striking section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ) and inserting section 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ) .",
      "versionDate": "2025-11-18",
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
        "actionDate": "2025-11-21",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6266",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Algorithm Accountability Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-04T15:54:59Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3193is.xml"
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
      "title": "Algorithm Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T05:08:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Algorithm Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-02T05:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 230 of the Communications Act of 1934 to limit liability protection under that section for certain social media platforms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-02T05:03:19Z"
    }
  ]
}
```
